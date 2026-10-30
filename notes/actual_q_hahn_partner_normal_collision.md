# The actual partner normal is transverse to a generic collision

30 October 2026. The large partner in the original mixed-circle column
can be compared with the small column BEFORE specializing q. Their
equality holds on a generic spectral-collision hypersurface. This gives
an exact transverse derivative formula for the original first normal,
and an explicit finite tail. The tail has genuine additional poles;
there is no individual-normal holomorphic theorem on the entire joint
central wedge.

No polynomial relative bound for that normal on a smaller corridor is
proved here. Nor does a pole of an individual continued column imply a
pole of the full physical coupon after all measures and terms are combined.

## 1. The original generic column in a symmetric finite form

Use Q=zeta^2, d=N-1, B=Q^(-N), x=zeta^d, U=Q^u,
T=Q^t and X=U^(-1). Write (a;Q)_k=product_(r=0)^(k-1)(1-a Q^r).
The actual generic Clebsch column from
[the mixed compiler](actual_mixed_augmented_plat_compiler.md), section 2,
has the finite expression

    C_m=x^u F_m,
    F_m(Q,B;X,T)=sum_(k=0)^m
       (Q^(-m);Q)_k (B^2 Q^(m+1);Q)_k (X;Q)_k Q^k
       /[(BQ;Q)_k (T^(-1);Q)_k (Q;Q)_k].              (1)

In (1), B is temporarily an independent variable. Its specialization
B=Q^(-N) is the ORIGINAL generic source; B is not a replacement
quantization. All displayed denominator factors are units near a
primitive N-th root with B=1, except the indicated T divisors.

For clarity, the finite transformation in (1) has a direct proof.
The original bivariate numerator is

    H_m^B(U,V)=sum_(a=0)^m (-1)^a B^a Q^[a(a+1)/2]
       [m choose a]_Q (BQ^(m-a+1);Q)_a/(BQ;Q)_a
       V^a product_(r<a)(U-Q^r)
           product_(r<m-a)(V-Q^r),
    F_m=H_m^B(U,T/U)/product_(r<m)(T-Q^r).             (2)

The normalized generic Casimir operator, after removing x^u, has
eigenvalues Lambda_m=B^(-1)Q^(-m)+B Q^(m+1). On the Newton basis
P_k(X)=(X;Q)_k its action is triangular:

    L P_k=Lambda_k P_k+eta_k P_(k-1),
    eta_k=(B^(-1)-Q^k)(1-Q^(k-1)/T)(1-Q^(-k)).         (3)

One can check the lower term without a summation transformation.
At X=1,Q^(-1),...,Q^(2-k), the shifted polynomial vanishes, so
the lower term is divisible by P_(k-1). At X=Q^(1-k), only the
X/Q shift remains; its coefficient is
(B^(-1)-Q^k)(1-Q^(k-1)/T), and
P_k(X/Q)/P_(k-1)(X)=1-Q^(-k). The leading coefficient gives Lambda_k.

Consequently the coefficients of a degree-m eigenfunction normalized
to F_m(1)=1 satisfy

    a_(k+1)/a_k=Q(1-Q^(k-m))(1-B^2 Q^(m+k+1))
       /[(1-BQ^(k+1))(1-Q^k/T)(1-Q^(k+1))].            (4)

For generic parameters these eigenvalues are distinct. The degree-m
normalized eigenfunction is unique, and (4), with a_0=1, gives (1).
Rational continuation then proves the identity wherever defined.

There is no small-channel restriction hidden in this argument. To
justify the generic operator identity for a fixed arbitrary m, first
take every integer source size N>=2m+1. The original generic Clebsch
calculation and its sufficiently many complete physical t slices give
the identity at B=Q^(-N), after clearing denominators. The cleared
residual is a FIXED finite Laurent polynomial in B,Q,U,T. Write it
as sum B^a p_a(Q,U,T). For N larger than its finite Q-exponent
widths, the supports of Q^(-Na)p_a are disjoint. Its vanishing at
all such N forces every p_a=0. Thus (3) and the actual numerator
identity are formal in B,Q, and apply equally to a large m<N.
The physical slice count at one fixed N is not being applied to a
large partner.

## 2. The collision identity is generic

Fix 0<=j<l and j+l=N-1. The eigenvalue difference factors as

    Lambda_l-Lambda_j
      =B^(-1)Q^(-l)(1-Q^(l-j))(1-B^2 Q^N).            (5)

On the generic hypersurface B^2 Q^N=1, the two numerator parameters
of (1) for m=j are the two numerator parameters for m=l in the
opposite order. In the large series the second parameter is Q^(-j),
so its terms k>j vanish. Therefore, IDENTICALLY in X,T,

    F_l=F_j on B^2 Q^N=1.                             (6)

Work locally near the actual primitive root Q_0, B=1, with the
denominators in (1) inverted. The collision is smooth there because
its B derivative is nonzero. Equation (6) gives a regular rational
function R_(j,l) such that

    F_l-F_j=(1-B^2 Q^N) R_(j,l).                       (7)

At even N another algebraic component of the collision can meet
denominator divisors. This does not affect the stated local germ:
every factor 1-BQ^r, 1<=r<N, is a unit at Q_0,B=1. The assertion
does not cancel a denominator identically zero on an irrelevant
component.

At the actual root, (6) also proves the useful bivariate factorization

    H_l^1(U,V)=H_j^1(U,V)
                     product_(r=j)^(l-1)(UV-Q_0^r).    (8)

This is an identity of the continued source numerator, not just an
equality on the physical integer magnetic grid.

## 3. The actual generic-q normal becomes a transverse B derivative

Return to B=Q^(-N), q=exp(pi i/N), Q_0=q^2, x=q^(N-1), and put

    Delta=q^(2j+1)-q^(-2j-1), D=zeta d/dzeta.

The actual tensor Casimir eigenvalue is

    lambda_m(zeta)=zeta^(2N-2m-1)+zeta^(-2N+2m+1),
    D(lambda_j-lambda_l)(q)=-2N Delta.

The root-only expression q^(2m+1)+q^(-2m-1) has the same value but
would give the WRONG derivative sign. The actual mixed compiler uses

    w_j=[D C_j(q)-D C_l(q)]/[-2N Delta].              (9)

Along this ACTUAL generic family,

    D(1-B^2 Q^N)=2N at the root.

Since F_l-F_j vanishes identically in X,T on the collision, the
derivatives of x^u, X=zeta^(-2u), and T=zeta^(2t) do not contribute
to the derivative of the difference. Equations (7),(9) give exactly

    w_j=x^u R_(j,l)(Q_0,1;X,T)/Delta
       =x^u [B partial_B(F_j-F_l)]_(Q_0,1)/(2 Delta).   (10)

The partial derivative in the second line holds Q,X,T fixed. This
is an exact consequence of generic collision divisibility. It is
NOT differentiation of the root-only identity F_l=F_j. In particular
the large partner's generic normal has not been dropped.

## 4. The explicit surviving derivative tail

All expressions in this section are at Q=Q_0. Put

    a=Q^(-j), b=Q^(-l),
    c_k=(a;Q)_k(b;Q)_k(X;Q)_k Q^k
                         /[(Q;Q)_k^2(T^(-1);Q)_k],
    L_k(y)=-sum_(r=0)^(k-1) y Q^r/(1-y Q^r).

For k<=j, every factor in L_k(a),L_k(b) is a unit. Differentiating
(1) in B and subtracting cancels the common denominator derivative.
For k>j the single vanishing numerator factor has derivative

    [y partial_y(y;Q)_k]_(y=Q^(-j))
                    =-(a;Q)_j(Q;Q)_(k-j-1).

Thus the ORIGINAL normal is

    w_j=x^u/Delta * {
       sum_(k=0)^j c_k [L_k(b)-L_k(a)]
       +(a;Q)_j sum_(k=j+1)^l
          (b;Q)_k(Q;Q)_(k-j-1)(X;Q)_k Q^k
                          /[(Q;Q)_k^2(T^(-1);Q)_k] }. (11)

The second line is a nonempty tail whenever j<l. Bounded harmonic
coefficients in the first line do not bound this coherent sum
relative to F_j; nor do they remove the tail. Equation (11) records
all of it with the original normalizer.

## 5. Genuine extra poles obstruct a whole-wedge normal theorem

As a polynomial in X, w_j/x^u has EXACT degree l. Only the k=l
tail term contributes its highest coefficient, which is

    (-1)^l Q^[l(l+1)/2]
       (Q^(-l);Q)_l(Q^(-j);Q)_j(Q;Q)_(l-j-1)
       /[Delta (Q;Q)_l^2(T^(-1);Q)_l].                (12)

Its numerator is nonzero: all nonzero factorial indices are less
than N, and 2j+1<N gives Delta!=0. Therefore each divisor

    T=Q^r,                 j<=r<l,                    (13)

is a genuine SIMPLE pole of the normalized normal for generic X.
The highest-coefficient residue is nonzero and cannot be canceled
by lower powers of X. Its residue polynomial has degree l, so it
does not vanish on an open set of magnetic coordinates.

The ordinary small column F_j has no pole at any of (13). Its
denominator only uses r<j. If N/2<r<l, the scaled pair degree
tau=r/N lies strictly inside the joint central wedge. An open set
of its central magnetic coordinates avoids the finitely many roots
of the residue polynomial. Thus the actual terminating continuation
of this INDIVIDUAL first normal cannot be holomorphic on that whole
wedge, let alone admit a uniform relative polynomial estimate there.

These additional divisors lie below the physical high-partner range
t>=l. On a fixed compact tau>1/2 they disappear when j/N is
sufficiently close to 1/2. Consequently (13) does not disprove a
smaller corridor near the folded endpoint. It also does not prove
such a corridor estimate: the tail in (11) still requires control.

Finally, (13) is not a theorem about poles of the entire mixed
coupon. The original inverse measure and the other terms may cancel
individual-column poles. Nor does it exclude a separately specified
whole-source continuation. It rules out silently extending the
ordinary-column joint theorem to this canonical generic normal.

Audit: [generic collision, original normal and pole certificates](../experiments/audit_actual_q_hahn_partner_normal_collision.py).

Independent analytical review and fresh audit: PASS. A second reader
rederived the Newton-basis coefficient ratio, checked the fixed-degree
Laurent-support extension, actual eigenvalue-gap sign, transverse factor,
core and tail signs, and the noncanceling highest-coefficient poles.
The fresh audit passed 4,123 original generic-q normal comparisons,
445 nonphysical tail checks and 614 nonzero extra-pole residues, as
well as the generic transformations and noncyclotomic collisions.
No smaller-corridor estimate or full-coupon pole is inferred.

Primary-agent independent analytical review and fresh replay: PASS.
It checked the actual-source ratio recurrence and all-degree extension,
the tensor-eigenvalue gap convention, transverse derivative and tail
factor two, and the nonzero leading pole residues. The same focused
audit counts passed; the stated scope is unchanged.
