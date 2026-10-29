# The actual pretzel winding period and its explicit positive saddle family

**Subsequent global proof.** The
[coherent circle and period theorem](actual_pretzel_coherent_circle_and_period_asymptotic.md)
now proves survival for this complete augmented source, with explicit
nonzero leading constant and original normalization. The local symbol
calculations below alone do not imply that result; its additional
finite transformation, global recurrence bound and Gaussian estimates
are supplied in the linked proof.

29 October 2026. The complete augmented odd-pretzel source has an exact
one-variable residue with finitely many integer windings. Its literal
factorial coefficients give a positive-shape stationary family for every
fixed odd number of boxes. The action and the full Hessian can be computed
explicitly. This identifies candidate exponential rates of the ORIGINAL
period; it does not prove that its selected cycle has a nonzero coefficient
at those saddles or that every other contribution is smaller.

In particular a proposed strict radial-homotopy boundary gap is false:
an original diagonal face has the same action height. That face must be
combined with the interior contribution using the exact source, not
discarded as exponentially small.

## 1. Exact winding, including its normal multiplicity

Use N>=2, d=N-1, q=exp(pi*i/N), Q=q^2, kappa=q^(d^2/2), and
M=floor(d/2). The [literal complete base polynomial](actual_pretzel_complete_base_casimir_polynomial.md)
is denoted z_N(z). It is the actual quarter-turn of R^(-1)L_N,
with degree at most M and every scalar retained. For s odd boxes the
unchanged raw marked source is

    A_(N,s)=Phi_2(z_N^s),
    Phi_2(F)=(-1)^d N^2 [z^d](F mod P_N),
    P_N(z)=2T_N(z/2)+2.

The [full commutant and marked-trace proof](actual_pair_casimir_commutant_and_rotated_trace.md)
establishes this on all physical channels, not a semisimple projection.
Any existing external framing/peripheral line still multiplies A_(N,s).

Polynomial division or residues at infinity give EXACTLY

    Phi_2(F)=(-1)^d N^2/(2*pi*i) integral F(z)/P_N(z) dz,       (1)

around every finite node. Put z=w+w^(-1). On |w|=R>1 this is a
positively oriented ellipse enclosing those nodes, and

    P_N(w+w^-1)=(1+w^N)^2/w^N.

Consequently

    A_(N,s)=(-1)^d N^2/(2*pi*i) integral_(|w|=R)
       z_N(w+w^-1)^s w^N(1-w^-2)/(1+w^N)^2 dw.               (2)

The full squared denominator is compulsory. Expanding it on |w|>1
gives the finite coefficient identity

    A_(N,s)=(-1)^d N^2 sum_(m>=1) (-1)^(m-1)m
       ([w^(mN-1)]-[w^(mN+1)]) z_N(w+w^-1)^s.               (3)

Only m<=floor((sM+1)/N) can occur. At fixed odd s these are eventually
m=1,...,(s-1)/2. The coefficient m is the retained confluent/normal
source. There is no authorization to keep only m=1 before estimating
the others. The existing complete-base audit checks (3) against literal
original sources at all tested even and odd levels.

An immediate exact upper bound is

    |A_(N,s)| <= N^2 (R+R^-1)/(1-R^-N)^2 * R^-N
                       *max_(|w|=R)|z_N(w+w^-1)|^s.          (4)

The [coherent capacity diagnostic](actual_pretzel_coherent_radial_capacity_diagnostic.md)
tests (4) with the actual polynomial and all normal channels. A sampled
circle maximum is not a certified analytic upper bound.

## 2. The phase comes from the literal finite coefficient

Write F_a=(Q;Q)_a. The complete-base theorem gives

    kappa*z_N(w+w^-1)/N^2
      =sum_(v=0)^M sum_(r=0)^v
        F_(2v)/F_v^4 *
        (Q^-v;Q)_r(qw;Q)_r(q/w;Q)_r Q^r/F_r^3.              (5)

The positive continuant coefficient used to prove this simplifies to

    b_v=N^2 |F_(2v)|/|F_v|^4.

Indeed the original cosine product is
(Q^(v+1);Q)_(d-2v)=F_(d-v)/F_v=N/|F_v|^2. The fixed phase in
the continuant then gives b_v x^v=N^2F_(2v)/F_v^4. This removes
no phase from the finite sum (5).

Set X=exp(2*pi*i*v/N), Y=exp(2*pi*i*r/N). On a regular compact
subdomain the leading phase of a summand in (5), derived by integrating
its exact factorial/Pochhammer logarithms, is

    S(X,Y;w)=-6Li_2(1)-Li_2(X^2)+4Li_2(X)+Li_2(1/X)
       -Li_2(Y/X)+Li_2(w)+Li_2(1/w)
       -Li_2(wY)-Li_2(Y/w)+3Li_2(Y).                         (6)

The exponent convention is exp[N*S/(2*pi*i)]. At the points below use
principal dilogarithms continued on their indicated upper/lower sides.
The overall kappa^-1 contributes a real leading action constant pi^2,
and thus does not change the volume rate. Endpoint-uniform expansions
and contour selection do not follow from the interior phase calculation.

Its exponentiated logarithmic derivatives are

    exp(S_logX)=(1+X)^2/[(X-1)(X-Y)],
    exp(S_logY)=(1-Y/X)(1-wY)(1-Y/w)/(1-Y)^3,
    exp(S_logw)=(wY-1)/(w-Y).                               (7)

These also follow directly from the exact consecutive-term ratios in
(5). They are algebraic equations for the stationary support, with the
logarithmic marks still to be specified.

## 3. All box counts have an explicit positive-shape stationary branch

For one winding m with 0<m<s/2 put

    alpha=pi*m/s, eta=2 asinh(tan alpha),
    beta=atan(sec alpha),
    w_*=-exp(eta), Y_*=exp(2i beta),
    X_*=(Y_*-1)/(Y_*+3)=i sec(alpha)/(2-i sec(alpha)).          (8)

Then |Y_*|=1, |X_*|<1 and

    0<arg Y_*<arg X_*<pi.

Eliminating X from the first two equations in (7) gives

    Y=(3X+1)/(1-X),
    w+w^-1=6-16Y/(1+Y)^2.                                 (9)

With U=exp(2*pi*i*m/s), the third equation gives
Y=(Uw+1)/(w+U). Substitution factors exactly as

    (w-1)^2[(U+1)^2w^2-2(U^2-6U+1)w+(U+1)^2]=0.

The positive branch (8) is the root outside the unit circle and obeys

    w+w^-1=2-16U/(1+U)^2=2-4 sec^2(alpha).                   (10)

The factor w=1 is not silently identified with this branch.

There is an essential inner mark: on the specified dilogarithm sheets,

    S_logX=0, S_logY=2*pi*i, S_logw=2i alpha.                (11)

Thus the genuinely stationary marked phase for the s separate factors
of z_N^s is

    W_m=sum_(i=1)^s [S(X_i,Y_i;w)-2*pi*i Log Y_i]
                                      -2*pi*i*m Log w.     (12)

Equation exp(S_logY)=1 does not justify omitting that mark. At (8)
it changes only the real part of the action, since |Y_*|=1.

## 4. Exact action and nondegeneracy

Let Lambda(theta)=-integral_0^theta log|2sin t|dt. The action on (8) is

    Im W_m=8s [Lambda(pi/4+alpha/2)+Lambda(pi/4-alpha/2)].    (13)

One direct proof uses the stationary equations with their marks. For
the action per box, differentiation in alpha gives

    dV/dalpha=-2log|w_*|=-4asinh(tan alpha).

Elementary differentiation of the right side of (13), divided by s,
gives the same derivative. Both sides tend to zero as alpha tends to
pi/2; on the phase side this follows from dilogarithm inversion and
(pi-2alpha)log|w_*|->0. This fixes the additive regulator constant.
In particular s=3,m=1 gives 4v_8, where v_8=8Lambda(pi/4).
Among this specified positive branch family the action strictly decreases
with m, so m=1 has the largest action. This is not a classification of
every complex or endpoint contribution of the original cycle.

The Hessian is nondegenerate, without an assumed Gaussian coefficient.
In logarithmic coordinates (X,Y,w), let H_3 be the Hessian of S and H_2
its X,Y block. On the stationary loci,

    det H_3=-Y(Y-1)(Y+3)^2(w^2-6w+1)
                   /[4(w-Y)(Y+1)^2(Yw-1)],
    det H_2=-Y^2(Y+3)^2(w-1)^2
                   /[(w-Y)(Y+1)^3(Yw-1)].                 (14)

All factors are nonzero at (8). The effective outer Schur entry is
i cos(alpha). For the full 2s+1 variables of (12), block elimination
therefore gives

    det Hess W_m=s (det H_2)^(s-1) det H_3 !=0.             (15)

These are local phase statements. A nondegenerate stationary point
with nonzero local factorial amplitude is not yet a nonzero coefficient
in the selected original global period.

## 5. The equal-height original face is a genuine remaining obstruction

The proposed shift of log|X| from zero to log|X_*| cannot be justified
by a strict boundary gap. For every upper unit Y and
X=(Y-1)/(Y+3), the X-dependent part of (6) has exactly the SAME
imaginary part as at X=Y. The original diagonal edge X=Y has its
unique maximum at Y_*. Hence it reaches the height of the shifted
interior stationary point for every w_*<-1.

The [independent exact boundary calculation](actual_pretzel_radial_boundary_gap.md)
proves this identity with its branch marks. The actual r=v summand
in (5) is nonzero, and its endpoint residue survives the exact
factorial interpolation. It cannot be dismissed as an exterior zero
or an exponentially smaller boundary prism.

The next analytic requirement is to combine that diagonal-face period
and the interior contribution coherently, or eliminate the redundant
inner sum by an exact transformation. Until this is done, (13)--(15)
and numerical agreement with (4) do not prove augmented-base survival,
and still less the volume limit after fixed long fillings.

[Audit](../experiments/audit_actual_pretzel_winding_phase_and_geometric_saddles.py)
checks the algebraic elimination, all logarithmic marks, Hessian factors,
and the action formula. Exact finite winding/source checks remain in
the linked complete-base audit. No selected-cycle claim is inferred.
