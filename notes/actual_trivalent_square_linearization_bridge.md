# A short finite square-linearization proof of the positive source scalar

29 October 2026. This proves the remaining source-coefficient-to-short-series
identity by finite product linearization and root cancellation. It is
independent of the Jackson-Leibniz/Newton derivation. The input is the
already proved original-source coefficient theorem, not a proposed 6j
formula. All root denominators and zero coefficients are retained.

Put N>=2, d=N-1, Q^N=1 with Q primitive, F_k=(Q;Q)_k. Take retained
triangle labels a,b,c<=floor(d/2), let J=a+b+c, delta=J-d>=0,
r=b+c-a, and H=2c-r=a+c-b=d-2b+delta. In particular

    0<=delta<=min(a,b,c,H), 0<=r<=2min(b,c), 2b,2c<N.

The reversed coefficient in the
[actual root-Fourier theorem](actual_trivalent_root_fourier_source_certificate.md)
is

    C_delta=[U^delta](UQ^-b;Q)_b^2
       *sum_(e=0)^H [V^e](V;Q)_c^2
                         F_(2c-e)/F_(H-e) U^e.       (1)

The first three sections prove exactly

    C_delta=T_0 H_c,
    T_0=Q^[delta(delta-1-2b)] F_b^2 F_(2c)
                         /[F_H F_delta F_(b-delta)^2],
    H_c=sum_(k=0)^delta
      (Q^-delta,Q^-c,Q^-c,Q^-H;Q)_k Q^k
                  /(Q,Q^-2c,Q^(b-delta+1),Q^(b-delta+1);Q)_k. (2)

Every denominator here is nonzero. No ordering such as a=max(a,b,c)
is required. Section 4 completes the finite Sears transformation and
explicit phase conversion to the positive factorial partition.

## 1. An elementary finite product linearization

For generic v and nonnegative m,n,

    (U;v)_m(U;v)_n
      =sum_(k=0)^min(m,n) A_(m,n,k) U^k(U;v)_(m+n-k),
    A_(m,n,k)=(-1)^k v^[k(k-1)/2]
                 (v;v)_m(v;v)_n
              /[(v;v)_k(v;v)_(m-k)(v;v)_(n-k)].      (3)

Here is a finite induction. The m=0 case is immediate. With S=m+n,

    (1-v^m U)U^k(U;v)_(S-k)
      =U^k(U;v)_(S+1-k)
         +(v^(S-k)-v^m)U^(k+1)(U;v)_(S-k).

Consequently the next coefficient is

    A_(m,n,k)+(v^(m+n-k+1)-v^m)A_(m,n,k-1)
                                              =A_(m+1,n,k).

Substitution of the displayed factorials proves this equality; the
interior ratio is (1-v^(m+1))/(1-v^(m+1-k)). Endpoints follow by
clearing denominators and setting out-of-range coefficients to zero.
Thus (3) is a polynomial identity, and specializes at Q with m=n=c
because c<N. The largest product length 2c is also below N here.

Apply the coefficient multiplier

    V^e -> F_(2c-e)U^e/F_(H-e), 0<=e<=H,

to (3) with m=n=c, discarding coefficients above H. In its k-th term
the finite binomial coefficient [2c-k choose e-k]_Q cancels the
factor F_(2c-e). The remaining finite binomial theorem gives

    sum_(e=0)^H [V^e](V;Q)_c^2 F_(2c-e)U^e/F_(H-e)
      =sum_(k=0)^min(c,H) (-1)^k Q^[k(k-1)/2]
          F_c^2 F_(2c-k)
          /[F_k F_(c-k)^2 F_(H-k)] U^k(U;Q)_(H-k).  (4)

No coefficient beyond the genuine derivative range H is introduced.

## 2. The exact root coefficient cancellation

For 0<=n<=b put

    I_n=[U^n](UQ^-b;Q)_b^2(U;Q)_(d-2b+n).

Since (U;Q)_N=1-U^N and n<N, coefficient extraction gives exactly

    I_n=[U^n] (UQ^-b;Q)_b
                        /(UQ^(n-1-2b);Q)_(b+1-n).  (5)

Indeed the missing factor in the length-N product runs from exponent
n-1-2b through -1. Its last b factors cancel one of the two numerator
products. Formal division is valid because every Euler factor has
constant coefficient one. The discarded numerator term U^N cannot
affect the coefficient n.

Set h=b+1-n>=1 and z=Q^(n-1-2b). The reciprocal finite-product
coefficient is z^l(Q^h;Q)_l/F_l: it follows either by multiplying
the factors, or from the recurrence obtained by shifting U to QU.
Expanding the numerator in (5), and dividing by its v=0 term, gives

    I_n=z^n (Q^h;Q)_n/F_n
                       *sum_(v=0)^n (Q^-n;Q)_v Q^[(b+1)v]/F_v.

The factors (Q^-b;Q)_v cancel in numerator and denominator; they
are nonzero since v<=n<=b<N. The finite binomial theorem evaluates
the sum as (Q^(b+1-n);Q)_n=(Q^h;Q)_n. Therefore

    I_n=Q^[n(n-1-2b)] F_b^2/[F_n F_(b-n)^2].         (6)

This proof includes n=0 and uses no analytic limit or infinite series.

## 3. Consecutive terms give the exact short series

Insert (4) into (1). Only k<=delta contributes, and put n=delta-k.
Since H-k=d-2b+n, equation (6) applies term by term. The result is

    C_delta=sum_(k=0)^delta T_k,
    T_k=(-1)^k Q^[k(k-1)/2+(delta-k)(delta-k-1-2b)]
       *F_b^2 F_c^2 F_(2c-k)
       /[F_k F_(c-k)^2 F_(H-k) F_(delta-k) F_(b-delta+k)^2]. (7)

Every factor is a physical factorial with index in 0,...,d. The
initial term is precisely T_0 in (2). Its consecutive ratio is

    T_(k+1)/T_k
      =Q * (1-Q^(k-delta))(1-Q^(k-c))^2(1-Q^(k-H))
           /[(1-Q^(k+1))(1-Q^(k-2c))
                                  (1-Q^(b-delta+k+1))^2]. (8)

The apparent extra power in this ratio is Q^(H-delta+2b+2)=Q^(N+1)=Q.
This is exactly the root relation that is needed, rather than a
generic-q continuation of the root source. Equations (7),(8) prove (2).

All denominator ranges are safe: k+1<=delta<=c,b; 2c-k is positive
and below N for every ratio used; b-delta+k+1<=b<N. Empty sums and
delta=0 give the same formula without a ratio. This closes the finite
source coefficient bridge. Its remaining finite normalizations are
evaluated next. Physical CD and magnetic tensor normalizations remain
distinct from this scalar calculation.

## 4. The symmetric positive scalar, with its full original phase

Put r_1=a+b-c, r_2=H=a+c-b. In (2), use the root equality
Q^(b-delta+1)=Q^(-a-c), and apply the
[own finite Sears identity](finite_balanced_sears_operator_proof.md)
with length delta, retained parameter Q^-c, and both selected
denominators Q^(-a-c). It gives

    H_c=K_1 H_sym,
    K_1=(Q^-a,Q^(-a-b);Q)_delta
                        /(Q^(-a-c),Q^-r_1;Q)_delta,
    H_sym=4phi3(Q^-delta,Q^-a,Q^-b,Q^-c;
                           Q^(-a-b),Q^(-a-c),Q^(-b-c);Q,Q). (9)

Every descending denominator index is at least delta, and every upper
factorial index is below N. Thus this is a direct finite specialization.
No division by H_sym is used. Its kth term is strictly positive at
the principal root: the sine factors are positive, and their residual
phase is q^[k(J-delta+1)]=q^(Nk)=(-1)^k, cancelling the denominator's
remaining (-1)^k. The k=0 term is one.

Here is a short explicit normalization of the ACTUAL source. Let

    E_F=3a^2+b^2+c^2-2ab-2ac+2bc-2c-2,
    E_src=2a^2-ab-ac+bc-J-3,
    tau_u=(-1)^u q^[u(u+1)], F_u F_(d-u)=N tau_u.

The original Fourier theorem says

    A=N q^[E_F+2b(b+1)-2c(c-1)]
                         C_delta/(F_a F_b F_c F_r). (10)

Converting K_1 to factorials introduces NO phase: the sums of its
two numerator and denominator descending parameters agree. Explicitly

    K_1=F_a F_(a+b) F_(d-b) F_(d-2c)
            /[F_(a-delta) F_(d-c) F_(a+c) F_(r_1)].

Insert T_0 from (2) into (10) and reflect complements. Its remaining
factorial prefactor is exactly

    N^2 tau_b tau_(2c) tau_(a+b)/(tau_c tau_(a+c))
      /[F_r F_(r_1) F_(r_2) F_delta
                           F_(a-delta) F_(b-delta) F_(c-delta)]. (11)

The tau signs multiply to (-1)^(2b)=1. The seven denominator indices
sum to 2d, so F_u=(-i)^u q^[u(u+1)/2]s_u contributes the net sign
(-1)^d. If E_total is the remaining q exponent, direct expansion gives

    E_total-E_src+N(J+1)=2N(2b+1).

Thus the exact phase of (11), including (10), is
(-1)^(N+J)q^E_src. Its positive modulus proves

    A=(-1)^(N+J)q^E_src D_sym H_sym,
    D_sym=N^2/[s_r s_(r_1)s_(r_2)s_delta
                         s_(a-delta)s_(b-delta)s_(c-delta)]>0. (12)

This proves nonvanishing on EVERY supported triangle, at both parities.

For completeness the same symmetric series is the positive R_N.
Choose a maximal label a for this SYMMETRIC positive object. Its first
term and the first finite Sears prefactor are

    R_0=s_a s_(b+c)/[s_(a-b)s_(a-c)s_b s_c s_r],
    K_0=(Q^(a+1),Q^-2b;Q)_r
                              /(Q^(a-b+1),Q^-b;Q)_r.

The long series is obtained by the consecutive ratio of the seven
sine-factorial summand. The proved Sears identity changes it to H_b,
and the same identity changes H_b to K_2 H_sym, where

    K_2=(Q^-c,Q^(-a-c);Q)_delta
                         /(Q^(-b-c),Q^-r_2;Q)_delta.

The finite denominator ranges are safe since r<=b,c and delta<=r_2.
The phases in K_0 and K_2 cancel internally, so both are positive.
Their sine-factorial products and reflection s_u s_(d-u)=N give

    R_0 K_0 K_2
      =N^3/[s_a s_b s_c s_r s_(r_1)s_(r_2)
                         s_(a-delta)s_(b-delta)s_(c-delta)]. (13)

Both sides are symmetric; the choice of a maximal chart places no
restriction on the source ordering. Combining (12),(13) proves the
original all-channel identity

    A=(-1)^(N+J)q^E_src [s_a s_b s_c/(N s_delta)]R_N.

The source is zero for J<d by the independent Fourier degree theorem.
This entire finite proof concerns the actual black scalar. It does
not bound its magnetic tensor or replace the marked white co-source.

Audit: [finite product, weighted coefficient and root bridge](../experiments/audit_actual_trivalent_square_linearization_bridge.py). The separate [full-source audit](../experiments/audit_actual_trivalent_general_scalar_candidate.py) compares the final phase and normalization with original coproduct columns. The finite proofs establish the all-parameter identities; these checks supplement them.