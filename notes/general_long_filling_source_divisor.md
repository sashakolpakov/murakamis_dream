# Long filling across a finite-order zero of the original source amplitude

30 October 2026. The general original-source filling theorem does not
need its leading analytic amplitude to be a unit at the complete point.
A NONZERO amplitude germ is sufficient away from its pulled-back
analytic zero set. That exceptional set occupies density zero among
large signed integer slope boxes. Suitable rational rays avoid it
eventually; a coordinate monomial times a unit avoids it at EVERY
independently sufficiently long slope tuple.

This removes one source hypothesis. It does not construct the required
whole-source gap or complex packet for an arbitrary plat, and it does
not prove that an unknown original source has a nonzero amplitude germ.
The source, its full normal terms and all peripheral factors remain the
ones in the [general transfer](general_original_source_long_filling_transfer.md).

## 1. The precise weaker packet hypothesis

Fix a diagram and a chosen nonempty set of b filled circle ports. Keep
the exact all-input full-twist identity, known nonzero outer factor
chi_N, entire physical color-complement gap, and exponentially accurate
finite corridor interpolation of the general transfer theorem.
The finite packet C_N is holomorphic and even separately in all b
coordinates on the SAME fixed complex neighborhood required there.
Replace only its relative unit-amplitude assumption by

    C_N(x)=N^mu exp[N phi(x)] [a(x)+r_N(x)],
    sup |r_N| <= C/N,                                      (1)

uniformly holomorphically on that neighborhood. Here a is a nonzero
holomorphic GERM, allowed to satisfy a(0)=0; phi is separately even,

    phi(0)=F0 real,
    phi''(0)=2pi i diag(tau_1,...,tau_b), Im tau_i>0.         (2)

The explicit original unit phase eta_N stays outside C_N, as before.
An absolute holomorphic remainder in (1) is essential. A pointwise
estimate on physical colors, or an estimate obtained by division by
an amplitude that vanishes, does not supply this hypothesis.

Separate evenness of a follows even if not assumed: the holomorphic
functions N^(-mu) exp[-N phi] C_N are separately even and converge
uniformly to a. The same is then true of r_N. Their fixed derivatives
are uniformly bounded on smaller domains by Cauchy's formula.
The upper Gaussian corridor estimate uses boundedness of a+r_N,
not a lower bound for a, so it remains valid.

If some auxiliary cusps are UNFILLED, first set their color variables
to zero in the actual packet and action. The amplitude required here
is the resulting restricted germ a_I(x_I)=a(x_I,0). A nonzero full
germ need not have a nonzero restriction: a(x_1,x_2)=x_2^2 vanishes
identically when only port 1 is filled. Such a restriction needs its
own first nonzero asymptotic coefficient; it is not covered by (1).

## 2. The actual filling map and its source divisor

Put epsilon_i=1/p_i for the fixed nonzero integer slopes. The minimal
charge source saddle xi(epsilon) solves

    phi_i(xi)+pi i epsilon_i(xi_i-1)=0, 1<=i<=b.            (3)

The analytic implicit-function theorem gives a unique small solution,
xi(0)=0, and DIRECT differentiation gives

    D xi(0)=diag(1/(2 tau_1),...,1/(2 tau_b)).               (4)

In particular xi is a local biholomorphism. The factor 2 in (4)
comes from the original full-twist convention and must be retained.

There is a stronger coordinatewise statement. Separate evenness writes
phi_i(x)=x_i psi_i(x), where psi_i is analytic and psi_i(0)=2pi i tau_i.
Equation (3) becomes

    xi_i=epsilon_i u_i(epsilon),
    u_i(epsilon)=pi i/[psi_i(xi(epsilon))+pi i epsilon_i],
    u_i(0)=1/(2 tau_i).                                    (5)

Every u_i is a unit on a sufficiently small common polydisk. Thus
xi_i is nonzero whenever epsilon_i is nonzero, independently of the
relative sizes and signs of the other coordinates.

Define the pulled-back source germ

    f(epsilon)=a(xi(epsilon)),
    Z={epsilon: f(epsilon)=0}.                             (6)

It is nonzero because xi is locally invertible. Therefore Z is a
proper complex analytic zero set, with its multiplicities supplied
by f. Multiplying a by a nowhere-zero analytic change of source
trivialization leaves Z unchanged. This is the source divisor used
here; it is not inferred from the classical A-polynomial.

The map (3) involves the marked analytic action and logarithmic
coordinates. Even if the exponentiated shape branch is algebraic,
Z is NOT asserted to be Zariski closed in epsilon or in the slopes.

## 3. Full-source transfer off the divisor

For every independently sufficiently long fixed signed tuple p with
f(1/p)!=0, the full original invariant has the SAME action and
N-power as the general transfer:

    K_N(p)=chi_N eta_N kappa^(-sum p_i)
        N^mu D(p) exp[N S_p] [1+O_p(N^-1)],                (7)

where

    S_p=phi(xi)+(pi i/2) sum_i (xi_i-1)^2/p_i.              (8)

The coefficient D(p) is nonzero. Its source-amplitude factor is
exactly a(xi); no value a(0) is inserted in its place.

Here is the required modification of the proof, rather than an
application of a theorem whose unit hypothesis has failed. Use the
same local Fourier critical map xi_F(z), action Psi(z), and determinant
branches as in the general transfer. Analytic finite-window stationary
phase applied to (1) gives the ABSOLUTE expansion

    F_N(z)=N^(mu+b/2) exp[N Psi(z)] [B(z)+O(N^-1)],
    B(z)=(2pi)^(b/2) a(xi_F(z)) /
                              sqrt(det[-phi''(xi_F(z))]). (9)

Both the remainder and its fixed derivatives are uniform on a smaller
fixed complex neighborhood. The proof expands the bounded analytic
amplitude a+r_N on the translated Gaussian contour, so it never
divides by a or B. Thus (9) is valid also on their zero sets.

Every global-color, finite-color-endpoint, noncentral Fourier and
large-charge estimate in the transfer uses an UPPER bound for C_N
and its controlled derivatives. Those estimates are unchanged by
(1). The strict ordering of nonminimal charges depends on phi,
not on a lower amplitude bound. For fixed p their exponential losses
dominate all the bounded amplitude factors.

At the second saddle use (9) in its absolute form. Put

    z_i*=(xi_i-1)/(2p_i),
    T_1(z)=Psi(z)-2pi i sum_i(p_i z_i^2+z_i).

Then T_1(z*)=S_p and the leading coefficient is

    D(p)=Gamma(p) a(xi),
    Gamma(p)=2^b (2pi)^b product_i sinh(2pi i z_i*) /
       [sqrt(det[-phi''(xi)]) sqrt(det[-T_1''(z*)])].      (10)

The determinants are nonzero on the chosen translated contours.
Equation (5) and smallness imply z_i* is nonzero for each finite p_i;
also |z_i*|<1/4, so its sinh factor is nonzero. Hence Gamma(p)!=0.
At fixed p with a(xi)!=0, division by this now NONZERO leading
coefficient turns the absolute O_p(N^-1) into the relative error in
(7). Its constant may increase as p approaches Z.

The 2^b minimal signed-charge sectors still ADD. Under a sign change
of one charge, its saddle coordinate changes sign; the exact packet
and its leading amplitude are separately even. The charge times
sinh factor, determinant branch and exact parity character have the
same transformation as in the original proof. This argument uses
the exact source symmetry, not positivity of a.

Consequently

    lim_N (2pi/N) log|K_N(p)|=2pi Re S_p.                   (11)

If the SAME source branch has the actual marked representation,
primitive peripheral equations and complete regulator anchor required
by the general geometric completion theorem, the right side is the
actual filled hyperbolic volume. Nothing in this amplitude extension
supplies those independent certificates.

Points in Z are excluded from this particular leading-coefficient
argument. They are NOT counterexamples to a volume limit: a later
Gaussian or source coefficient may give the same exponential rate.
The diagram and slopes remain fixed BEFORE N tends to infinity;
no joint large-N/large-slope uniformity is asserted.

## 4. Coordinate zeros permit every independently long slope

Suppose on the chosen filled-coordinate chart

    a(x)=product_i x_i^(2 nu_i) v(x), nu_i>=0,
    v(0)!=0.                                             (12)

The even powers are consistent with the actual separate evenness.
Combining (5) and (12) gives the exact germ factorization

    f(epsilon)=product_i epsilon_i^(2 nu_i) V(epsilon),
    V(0)!=0.                                             (13)

Thus EVERY independently sufficiently large signed nonzero tuple p
avoids Z, and uniformly over those tuples,

    c product_i |p_i|^(-2 nu_i) <= |a(xi(1/p))|
                              <= C product_i |p_i|^(-2 nu_i). (14)

No slope-comparability condition enters. The conclusion is therefore
as strong in its slope quantifier as the old unit-amplitude transfer.
For ONE filled cusp every nonzero separately-even analytic germ
automatically has the form (12), so the complete-point unit assumption
can always be dropped in that one-variable case.

For completeness the known filling prefactor also has a uniform
magnitude comparison. Here z_i*=(-epsilon_i/2)(1+O(||epsilon||))
and

    diag(epsilon_i) T_1''(z*)=-4pi i I+O(||epsilon||).

The other Hessian remains bounded and invertible. Formula (10) gives
|Gamma(p)| comparable to product_i |p_i|^(-3/2), on each signed
orthant, and hence on their finite union. Under (12), |D(p)| is
comparable to product_i |p_i|^(-2 nu_i-3/2). This is a statement
about the slope-dependent leading coefficient, not a uniform error
estimate when slopes grow with quantum level N.

## 5. Rational-ray survival for a general nonzero amplitude

Let d be the vanishing order of f at zero, including d=0 for a unit,
and let P_d be its first nonzero homogeneous Taylor polynomial. For
fixed nonzero signed integers q_1,...,q_b with

    P_d(1/q_1,...,1/q_b)!=0,                              (15)

the ray p_i=n q_i satisfies

    f(1/(nq))=n^(-d)[P_d(1/q)+O_q(n^-1)].                 (16)

Every sufficiently large n therefore avoids Z, with magnitude
comparable to n^(-d). Applying (7) separately at each fixed ray
point gives its full quantum volume limit whenever the geometric
certificates hold. The ray parameter n is not the quantum level N.

There is such a rational ray in EVERY prescribed sign orthant.
Indeed multiply P_d(1/q) by product_i q_i^d. The result is a
nonzero polynomial in the q_i. A nonzero polynomial cannot vanish
on the entire product of infinite one-sided integer sets: fix all
but one variable, use the finite root count, and induct on the number
of variables. This proves existence without assuming rational or
algebraic coefficients for P_d.

Condition (15) is sufficient, not necessary. A ray on which P_d
vanishes may have a nonzero higher-order coefficient in f.

## 6. Density one in every large signed integer box

Fix signs sigma_i. Among tuples

    p_i=sigma_i n_i, T<=n_i<=2T, n_i integers,

the number lying in Z is o(T^b) as the integer scale T tends to
infinity. Thus the proportion for which (7) applies tends to one.
This does not assert that ALL tuples avoid Z or that its exact
integer points lie in a fixed algebraic hypersurface.

Here is an elementary counting proof. Put t_i=n_i/T in [1,2].
Uniform analytic Taylor remainder estimates on this compact set give

    T^d f(sigma_1/(Tt_1),...,sigma_b/(Tt_b))
                         =P_d(sigma_1/t_1,...,sigma_b/t_b)+O(T^-1).

Therefore a bad tuple satisfies |Q(t)|<=C/T, where the NONZERO
polynomial

    Q(t)=product_i t_i^d P_d(sigma_1/t_1,...,sigma_b/t_b)

has no negative powers. Choose a nonzero real polynomial R from
the real or imaginary part of Q. On [1,3]^b its first derivatives
are bounded. To each bad grid point t attach the disjoint half-open
cube product_i[t_i,t_i+1/T). Every point of that cube then satisfies
|R|<=C'/T, with one fixed constant C'. Hence

    #bad/T^b <= volume{x in [1,3]^b: |R(x)|<=C'/T}.        (17)

A nonzero real polynomial has zero set of Lebesgue measure zero.
For a direct proof, write it as a polynomial in its last variable.
Except on the common zero set of its coefficients, contained in
the zero set of one nonzero lower-dimensional coefficient, every
fiber has finitely many roots. Induction and Fubini prove the claim.
The sublevel sets on the right of (17) decrease to that zero set,
so continuity of finite measure makes their volumes tend to zero.
This proves the stated density without a quantitative sublevel or
Diophantine theorem. The unit case d=0 is immediate as well.

## 7. Finite level classes and exact scope

The argument also covers finitely many level classes, for example
even and odd N, with the SAME phi and separate uniform expansions
(1) having nonzero germs a_r. All original class-dependent unit
phases are retained. Use the finite union of their divisors. Outside
it each class has (7), possibly with its own nonzero coefficient;
the exponential limit (11) holds along the full sequence.

The union still has density zero in each signed slope box. A
rational ray avoiding the product of the finitely many first nonzero
Taylor polynomials avoids every divisor eventually. If each amplitude
is a coordinate monomial times a unit, every independently long
tuple works at all the level classes. For partial fillings these
nonzero-germ checks must again be made AFTER restricting the unfilled
variables.

The advance is removal of the complete-point UNIT requirement,
including arithmetic survival of many long fillings. A proven
nonzero finite-order marked source amplitude can now be used even
when its complete value vanishes. The exact mixed source, its global
gap, its uniform complex packet and its actual geometric marking
remain necessary. No arbitrary-plat equality, whole knot A-polynomial
identification, or nonzero-source theorem is inferred from this lemma.

Audit: [implicit saddle, coordinate zeros and integer-slope examples](../experiments/audit_general_long_filling_source_divisor.py).
The density-one statement is proved by the analytic rescaling and
measure argument above, not by the finite counts in that audit.

The source and geometric hypotheses remain conditional as stated. They are not established here for arbitrary plats.