# The finite trivalent Euler coefficient to short balanced series

29 October 2026. This completes the missing finite coefficient identity
from the independent [root-Fourier source proof](actual_trivalent_root_fourier_source_certificate.md).
The proof uses only the coproduct Euler coefficient, finite Newton
interpolation, finite Vandermonde, and the
[own finite Sears lemma](finite_balanced_sears_operator_proof.md).
It does not import a 6j evaluation.

Set N>=2, d=N-1, Q=exp(2pi i/N), F_k=(Q;Q)_k. Let a,b,c be
nonnegative integers <=floor(d/2), satisfying the triangle inequalities,
and put

    r=b+c-a, delta=a+b+c-d>=0,
    r_1=a+b-c, r_2=a+c-b.

Thus delta<=min(a,b,c,r,r_1,r_2). Every finite factorial used below
has a physical index in 0,...,d. Write D_Q h(T)=[h(T)-h(QT)]/T and

    P=[T^d](TQ;Q)_b^2 D_Q^r (TQ^(1-c);Q)_c^2,
    C_delta=Q^[-b(b+1)+c(c-1)] P.                    (1)

The EXACT identity needed by the actual source normalization is

    C_delta=Q^[b(a+c-b)+c(2c+1)]
       *F_(2b)/F_(a+b-c)*F_a^2/[F_delta F_(a-delta)^2]
       *4phi3(Q^-delta,Q^-r,Q^-b,Q^-b;
                         Q^(-b-c),Q^(-b-c),Q^(-2b);Q,Q). (2)

The series terminates at min(delta,r). All denominator Pochhammers
are nonzero up to that length. No generic-q normal limit is taken.

## 1. Jackson Leibniz and a finite moment identity

The finite Leibniz formula follows by induction from
D_Q(uv)=(D_Qu)v+u(QT)D_Qv. Apply it to f(T)^2, f=(TQ^(1-c);Q)_c:

    D_Q^r f^2=(-Q^(1-c))^r F_c^2
      *sum_s [r choose s]_Q Q^[s(s-1)/2+(r-s)(r-s-1)/2]
       (TQ^(1-c+r);Q)_(c-s)
       (TQ^(1-c+r-s);Q)_(c-r+s)
                      /[F_(c-s)F_(c-r+s)].          (3)

Only max(0,r-c)<=s<=min(r,c) occurs. When multiplied by (TQ)_b^2,
the Euler product in a term of (3) is EXACTLY

    (TQ;Q)_b (TQ^(b-a+1);Q)_a
                         (TQ^(b-a-s+1);Q)_c.         (4)

To verify (4), compare exponent intervals using their endpoints;
the two sides have the same multiplicity at every integer exponent.
This argument works for EVERY triangle (a,b,c), not only a maximal
first label. Reversing degree J=a+b+c to degree delta in (4) gives
the three factors

    A(U)=(UQ^-b;Q)_b(UQ^-b;Q)_a,
    (UQ^(s-r);Q)_c.

The signs cancel since r+J=2(b+c). The full phase in this reversal
is

    P=Q^Z0 F_c^2F_r [U^delta]A(U)
       *sum_s w_s (UQ^(s-r);Q)_c,
    w_s=Q^[s^2-s(r+c)]/[F_sF_(r-s)F_(c-s)F_(c-r+s)],
    Z0=r(1-c)+r(r-1)/2+b(b+1)/2+ab-a(a-1)/2
                                      +c(b-a)+c(c+1)/2. (5)

The crucial moment is computed explicitly. The finite Newton identity

    x^ell=sum_(k=0)^ell (Q^-ell;Q)_k Q^k(x;Q)_k/F_k  (6)

follows by induction using x(x;Q)_k=Q^-k[(x;Q)_k-(x;Q)_(k+1)].
Put x=Q^(s-c), multiply by Q^(c ell), and sum against w_s.
The factor (Q^(s-c);Q)_k cancels F_(c-s), leaving Vandermonde
of lengths c-k and c. The exact result is

    sum_s w_s (Q^(s-c);Q)_k
      =(-1)^k Q^[-ck+k(k-1)/2-(c-k)r]
          F_(2c-k)/[F_rF_(2c-k-r)F_(c-k)F_c].        (7)

This is an own finite Vandermonde calculation: after cancellation,
its summand exponent is (c-k-s)(r-s), up to the displayed constant,
and the product-coefficient identity gives [2c-k choose r]_Q.
Out-of-range terms are zero. In the use below k<=delta<=2c-r, so
every displayed denominator is regular.

Expand (UQ^(s-r);Q)_c by the finite binomial theorem, insert (6),
and put ell=k+v. The remaining v sum is another FINITE Euler product.
Equations (6),(7) give

    sum_s w_s (UQ^(s-r);Q)_c
      =Q^(-cr) sum_k (-1)^k Q^[k(k-1)/2]U^k
       *F_(2c-k)(UQ^(c-r);Q)_(c-k)
                  /[F_rF_(2c-k-r)F_kF_(c-k)^2].     (8)

All sums here are finite, so their interchange has no convergence
hypothesis. In (5), the last Euler factor in (8) joins the length-a
factor contiguously, because c-r=a-b.

## 2. The root coefficient collapse

Let L=delta-k, so 0<=L<=b. The only remaining coefficient after
(8) is

    [U^L](UQ^-b;Q)_b(UQ^-b;Q)_(d+L-b)
       =Q^[L(L-1-2b)] F_b^2/[F_LF_(b-L)^2].          (9)

Here is a finite proof. Put M=d+L-b. The finite binomial expansion
of the left side, extracting its zeroth summand, is

    (-Q^-b)^L Q^[L(L-1)/2][M choose L]_Q
       *2phi1(Q^-L,Q^-b;Q^(M-L+1);Q,Q^(b+1)).

At this ROOT, Q^(M-L+1)=Q^(N-b)=Q^-b. The equal numerator and
denominator cancel, with no zero reached because L<=b<N. The
remaining finite binomial sum is (Q^(b+1-L);Q)_L. Converting its
two factors to F gives exactly (9). This is the source-specific
root collapse; no continuous-color replacement is used.

Combining (5),(8),(9), and writing

    Z=Z0-cr+delta(delta-1-2b)-b(b+1)+c(c-1),

one obtains

    C_delta=Q^Z F_b^2 F_(2c)
                    /[F_(r_2)F_delta F_(b-delta)^2] *H_c,
    H_c=4phi3(Q^-delta,Q^-r_2,Q^-c,Q^-c;
                            Q^(-a-c),Q^(-a-c),Q^(-2c);Q,Q). (10)

For example the raw kth term before normalization is

    (-1)^k Q^[k(k-1)/2+(delta-k)(delta-k-1-2b)]
       F_(2c-k)
       /[F_(2c-k-r)F_kF_(c-k)^2F_(delta-k)F_(b-delta+k)^2].

Its successive ratio gives (10); the residual argument is Q because
2+2b+2c-r-delta=N+1. This makes the root mark explicit.

## 3. Two proved Sears transformations meet at one symmetric series

Use the own finite Sears identity, with length delta, on H_c.
Keep Q^-c and choose d=e=Q^(-a-c). It gives

    H_c=K_1 H_sym,
    K_1=(Q^-a,Q^(-a-b);Q)_delta
                        /(Q^(-a-c),Q^-r_1;Q)_delta,
    H_sym=4phi3(Q^-delta,Q^-a,Q^-b,Q^-c;
                           Q^(-a-b),Q^(-a-c),Q^(-b-c);Q,Q).

The root equalities Q^(a+1-delta)=Q^(-b-c) etc fix all three
denominators. Applying the SAME finite Sears lemma to the H_b on
the right side of (2) gives

    H_b=K_2 H_sym,
    K_2=(Q^-c,Q^(-a-c);Q)_delta
                        /(Q^(-b-c),Q^-r_2;Q)_delta.  (11)

Every factorial index is physical, since delta<=a,b,c,r_i. Thus
neither transformation crosses a root pole. No division by H_sym
is needed; the comparison is between their explicit prefactors.

For clarity the complete phase cancellation is recorded. Let
tau_u=(-1)^u Q^[u(u+1)/2], so F_uF_(d-u)=N tau_u.
Converting (11) to factorials and reflecting complements gives

    [F_b^2F_(2c)/(F_(r_2)F_delta F_(b-delta)^2)](K_1/K_2)
     /[F_(2b)F_a^2/(F_(r_1)F_delta F_(a-delta)^2)]
      =tau_b^2 tau_(2c) tau_(a+b) tau_(b+c)
                           /(tau_(2b)tau_c tau_a tau_(a+c)^2)
      =Q^K,
    K=-a^2+ab-2ac-a+bc+b+c^2.

The residual sign is (-1)^[2(b-a)]=1. Finally direct expansion gives

    Z+K-[b(a+c-b)+c(2c+1)]
       =-(a-b+c+delta)(a+b+c-delta+1)
       =-N(-N+2a+2c+1).

Its Q power is ONE. Substituting into (10),(11) proves EXACTLY (2)
for every admissible supported triangle at both parities.

## 4. Fully symmetric, manifestly positive root form

The same calculation also removes every ordering qualification. No
step in (3)--(11) assumed a maximal first label. With the original
source phase

    E_src=2a^2-ab-ac+bc-J-3,

the actual scalar has the FULLY symmetric positive form

    A_source=(-1)^(N+J)q^E_src D_sym H_sym,
    D_sym=N^2/[s_r s_(r_1)s_(r_2)s_delta
                         s_(a-delta)s_(b-delta)s_(c-delta)]. (12)

Here q=exp(pi i/N), s_u=|F_u|. Every H_sym summand is POSITIVE:
in (Q^-u;Q)_k each factor is i q^(-u+l) times its positive sine.
The full term phase is q^[k(J-delta+1)]=q^(Nk)=(-1)^k, which
cancels the denominator phase (-1)^k. All descending sine indices
are nonnegative up to the true termination min(delta,a,b,c).
The zeroth term is one. Thus (12) proves nonvanishing for EVERY
supported triangle, at both parities and composite levels.

For an explicit check of the absolute normalization, insert K_2
from (11) and the source prefactor
Nq^[E+2b(b+1)-2c(c-1)]/(F_aF_bF_cF_r), with E from the Fourier
theorem, into (2). Reflect complementary factorials. Their modulus
is exactly D_sym. Their F-power difference is 1-N, and the remaining
q exponent, after (-i)^(1-N) is included, differs from
N(N+J)+E_src by 2N(-N+b+c+1). Hence the full phase is precisely
the one in (12), not merely an unspecified unit.

The positive candidate factorial sum, calculated in a chart with
a maximal label and then transformed by the same finite Sears lemma,
has

    R_N=N^3 H_sym/[s_a s_b s_c s_r s_(r_1)s_(r_2)
                         s_(a-delta)s_(b-delta)s_(c-delta)]. (13)

The long/short calculation and phase equivalence are recorded with
their explicit initial term in the
[finite candidate transform port](actual_trivalent_general_finite_transform_port.md#1-exact-long-and-short-series-for-the-candidate-factorial-object).
For a direct normalization check, in its maximal-a chart the initial
term is N s_a/[s_(a-b)s_(a-c)s_(a-delta)s_b s_c s_r]. Its first
Sears factor has modulus
s_(b+c)s_(2b)s_(a-b)s_(a-c)/[s_a s_(r_1)s_b s_c];
the phases of its two ascending and two descending Pochhammers
cancel exactly, so this factor is POSITIVE. The second factor K_2
in (11) is also positive: all four negative-parameter Pochhammer
phases cancel. Its modulus is
s_c s_(a+c)s_(d-a)s_(d-2b)
/[s_(c-delta)s_(d-b)s_(b+c)s_(r_2)].
Multiply these three displayed factors and use sine reflection;
the result is exactly the positive prefactor in (13).
Both sides of (13) are manifestly symmetric, so a maximal chart
can be chosen for ANY label order. Combining (12),(13) proves
A_source=(-1)^(N+J)q^E_src [s_as_bs_c/(N s_delta)]R_N
for every supported triangle. The lower-saturation branch is zero
by the independent complete-clock cancellation.

## 5. Original-source conclusion and its separate sewing scope

Together with the root-Fourier coefficient theorem and the explicitly
normalized candidate long-to-short series calculation, (2) proves
the positive trivalent scalar identity, rather than checking it at
finitely many levels. The scalar is zero for J<d; for J>=d it is the
specified unit phase times C_N R_N, hence NONZERO.

This scalar conclusion does not estimate the whole magnetic tensor:
its descendant coefficients can carry additional exponential
factorials. Ordinary white and marked white source contractions,
full Hermite normals and ordered graph sewing still retain their
actual independent data. In particular the scalar action maximum
must not be relabelled as an already proved full vertex norm bound.

Audit: [all finite coefficient stages and source phases](../experiments/audit_finite_trivalent_euler_racah_transform.py).

Root and independent internal proof reviews passed the complete
finite bridge, both Sears prefactors, all root denominator ranges,
the original source phase, positive symmetric series and every-label
extension. A fresh exact replay passed fifteen full supported root
families through N=16 at every intermediate finite stage, with a
symbolic check of the remaining phase multiple. The root's independent
[square-linearization proof](actual_trivalent_square_linearization_bridge.md)
reaches the same H_c without the Jackson-Leibniz/Newton route.
Tests are supplementary; the finite proofs establish the identity.
