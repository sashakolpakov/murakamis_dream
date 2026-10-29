# An independent audit of literature state integrals and their volume limits

Research note, 25 October 2026. No novelty claim is made. The definitions below
come from the cited literature. The estimates, contour arguments and algebraic
checks needed here are supplied separately; a published theorem is not being
used as its own proof.

There are three different conclusions:

* For the figure-eight knot, the specified Andersen–Kashaev state has the volume
  limit, and the explicit second-order literature operator is its minimal
  annihilator over the rational q-difference field, with the qualifications
  about analytic continuation below.
* A multivariate argument proves the volume limit for the explicit literature
  integral (4.5) of Ben Aribi–Wong whenever the stated finite matrix and positive
  geometric certificates are supplied. This includes the certified geometric
  FAMED class. The subsequent `general_annihilator_and_volume.md` proves
  existence of a minimal operator for these rescaled integrals in the
  Andersen–Malusà b-shift algebra, without an efficient coefficient formula.
* Neither argument proves a theorem for every alternating knot, nor establishes
  all the global topological identities of Teichmüller TQFT.

## 1. Fixed sources and conventions

1. Andersen–Kashaev, *A TQFT from quantum Teichmüller theory*,
   [arXiv:1109.6295v2](https://arxiv.org/pdf/1109.6295v2), Definition 15,
   equation (38), and Appendix A, equations (42)–(48).
2. Andersen–Malusà, *A Geometric Quantisation view on the AJ-conjecture for the
   Teichmüller TQFT*, [arXiv:1711.11522v3](https://arxiv.org/pdf/1711.11522v3),
   Definition 5 and Section 5.1. The algebraic certificate was checked against
   this version's TeX source. Corrections to other printed formulas in that
   version are discussed in `literature_definition_audit.md`.
3. Ben Aribi–Wong, *The Andersen–Kashaev volume conjecture for FAMED geometric
   triangulations*, [arXiv:2410.10776v2](https://arxiv.org/pdf/2410.10776v2),
   Definitions 1.1 and 2.7–2.10 and equation (4.5). Their asymptotic theorem is
   not assumed below.
4. Andersen–Kashaev, *Complex Quantum Chern–Simons*,
   [arXiv:1409.1208](https://arxiv.org/pdf/1409.1208), equation (122), fixes
   the finite-product convention for the level-N dilogarithm.

Take b>0, q=exp(2 pi i b^2), and

    hbar = (b+b^(-1))^(-2) = b^2/(1+b^2)^2.

The level-one boundary operators are

    Q f(x)=exp(-2 pi b x) f(x),     E f(x)=f(x-i b),
    E Q=q Q E.

Thus classical Q is m^2. All factors in Q are retained until after taking
operator identities. The complete point is Q=1 in this convention; it is not
an ideal point of the algebraic curve at infinity in the Culler–Shalen sense.

## 2. Quantum dilogarithm from its defining integral

Start with the literature definition

    log Phi_b(Z) = integral_(R+i0)
        exp(-2 i Z w)/(4 sinh(b w) sinh(w/b) w) dw.             (2.1)

The contour passes above zero. It can equally be taken on a sufficiently small
positive horizontal line. The exponential of this integral is holomorphic and
nonzero in |Im Z|<(b+b^(-1))/2. This assertion follows from locally uniform
convergence on a displaced contour, not from an asserted zero/pole formula.

### 2.1 A uniform complex remainder on an entire horizontal strip

For every delta>0 there is C_delta such that, for 0<b<=1 and
|Im z|<=pi-delta,

    log Phi_b(z/(2 pi b))
      = Li_2(-exp z)/(2 pi i b^2) + R_b(z),
    sup_z |R_b(z)| <= C_delta b^2.                            (2.2)

The logarithm is the one prescribed by (2.1), and the dilogarithm branch is
analytic on |Im z|<pi and tends to zero as Re z tends to minus infinity.
The supremum includes every real part of z.

**Proof.** Substitute w=b t into (2.1). Subtract the leading kernel to obtain

    I(z)=1/4 integral_(R+i0) exp(-i z t/pi)/(t^2 sinh t) dt,
    K_b(t)=1/(4 t sinh t) [1/sinh(b^2 t)-1/(b^2 t)].

First evaluate I without assuming a quantum-dilogarithm asymptotic. Put

    J(z)=integral_(R+i0) exp(-i z t/pi)/sinh t dt.

A rectangle translated upward by i pi gives

    (1+exp z) J(z)=-2 pi i exp z.

Indeed the integrand changes by -exp z on translation, and the enclosed pole
at i pi has residue -exp z. The vertical edges tend to zero for |Im z|<pi.
Consequently

    I''(z)=-J(z)/(4 pi^2)
          = i exp z/(2 pi(1+exp z)).

This is the second derivative of Li_2(-exp z)/(2 pi i). Both I and I' tend to
zero as Re z tends to minus infinity: move the t contour to Im t=a, 0<a<pi,
and use its exponentially decaying kernel. This fixes both integration
constants. The finite-part integrals at zero are thereby fixed by the upper
contour, rather than by an unspecified regularization.

On the positive real axis K_b is real, and its odd continuation has residue

    c_b^rem=-b^2/24

at zero. Write c=c_b^rem in the following formulas; this is not the usual
quantum-dilogarithm constant i(b+b^(-1))/2. Taylor expansion, uniformly for
0<b<=1, gives

    K_b(t)=c/t+O(b^2 t)                    (0<t<=1).

For t>=1 use |1/sinh v-1/v|<=C v for v>0, obtaining

    |K_b(t)|<=C b^2 exp(-t).

Define H_b(t)=K_b(t)-c exp(-t)/t. Then

    integral_0^infinity |H_b(t)| exp((1-delta/pi)t) dt
        <= C_delta b^2.

The clockwise upper indentation at zero contributes -i pi c. Pairing the
positive and negative halves of the real contour therefore yields the exact,
ordinary convergent formula

    R_b(z)=-2 i [ integral_0^infinity H_b(t) sin(z t/pi) dt
                         + c arctan(z/pi)] - i pi c.          (2.3)

Here integral exp(-t) sin(z t/pi)/t dt=arctan(z/pi), with the branch analytic
on |Im z|<pi. This arctangent is bounded on each smaller closed strip, including
as Re z tends to either infinity. The preceding weighted L1 bound controls
the remaining integral uniformly on that strip. This proves (2.2). QED.

Two normalization checks follow directly:

    R_b(0)=i pi b^2/24,
    R_b(z)+R_b(-z)=i pi b^2/12.                              (2.4)

Together with Li_2(-e^z)+Li_2(-e^(-z))=-pi^2/6-z^2/2, they give the exact
inversion identity, initially on the common strip,

    Phi_b(Z) Phi_b(-Z)
       = exp(i pi Z^2+i pi(b^2+b^(-2))/12).                  (2.5)

The scalar in (2.5) has modulus one for b>0. It has not been silently discarded
in an operator or state comparison.

### 2.2 Functional equation independently recovered

Subtract the logarithms (2.1) at Z-i b/2 and Z+i b/2. The factor sinh(bw)
cancels, leaving

    -1/2 integral_(R+i0) exp(-2 i b Z t)/(t sinh t) dt.

Its derivative in Z is 2 pi b exp(2 pi b Z)/(1+exp(2 pi b Z)), by the same
rectangle evaluation of J. Both it and log(1+exp(2 pi b Z)) vanish at the
left end of the strip. Hence

    Phi_b(Z-i b/2)
       =(1+exp(2 pi b Z)) Phi_b(Z+i b/2).                    (2.6)

The second functional equation follows by b<->b^(-1) in (2.1). Thus neither
the functional equation nor the normalization in (2.2) is imported from an
unchecked asymptotic theorem.

## 3. The exact literature figure-eight state

Equation (38) of Andersen–Kashaev defines

    chi_b(x)=integral_(R-i0) Phi_b(x-y)/Phi_b(y)
                                exp(2 pi i x(2y-x)) dy.      (3.1)

In the level-one convention used for the Andersen–Malusà boundary operators,

    J_b(x)=exp(4 pi i c_b x) chi_b(x),
    c_b=i(b+b^(-1))/2.                                     (3.2)

At x=0 the two states agree. Our volume theorem refers to this specified
state, rather than an arbitrarily chosen solution of a difference equation.

The level identification can be checked directly from the definition,
not just its functional equations: the finite product (122) in *Complex
Quantum Chern–Simons* has j=0,...,N-1 and argument

    x/sqrt(N)+(1-1/N)c_b-i b^(-1)j/N-i b{(j+n)/N}.

At N=1 and n=0 it is the single factor Phi_b(x). The change n->-n in
Andersen–Malusà is trivial at N=1, the Haar measure becomes ordinary Lebesgue
measure, and the Gaussian is exp(pi i y^2). Their Gaussian ratio equals
exp(2 pi i x(2y-x)). The algebra below also derives the
operator directly from (3.1)–(3.2), so it does not need an assumed general-N
identification or a general-N proof.

**Theorem 3.1.** As b tends to zero through positive real values,

    J_b(0)=chi_b(0)
      = 3^(-1/4) exp(-Vol(S^3\4_1)/(2 pi b^2)) (1+o(1)).    (3.3)

In particular

    lim -2 pi b^2 log|J_b(0)|
      = lim -2 pi hbar log|J_b(0)|
      = Vol(S^3\4_1)=2 D(exp(i pi/3)).                       (3.4)

Here D is the Bloch–Wigner dilogarithm. The geometric identification is the
two-regular-ideal-tetrahedron decomposition of the complete figure-eight
complement; its six tetrahedral edge angles around each edge sum to 2 pi.

**Proof.** Set u=2 pi b y and eta=2 pi/3. Move the contour to

    u=t-i eta,  -infinity<t<infinity.

Both u and -u remain in the fixed strip |Im u|<pi, where the defining
logarithms are holomorphic and nonzero. Equation (2.2) gives

    chi_b(0)=1/(2 pi b) integral_R
       exp(F(t)/(2 pi b^2))
       exp(R_b(-u)-R_b(u)) dt,
    F(t)=[Li_2(-exp(-u))-Li_2(-exp u)]/i.                    (3.5)

The last exponential is 1+O(b^2), uniformly for all t. The classical action
S(u)=i F(t) satisfies

    S'(u)=log(1+exp(-u))+log(1+exp u),
    S'(-i eta)=0,
    S''(-i eta)=-i sqrt(3).

On the stated line, the sum of logarithms is the continuous logarithm of
2+2 cosh(t-i eta). For t>0 that number has negative imaginary part, since
its imaginary part is -sqrt(3) sinh t. For t<0 its imaginary part is positive.
It follows that Re F has its unique global maximum at t=0, with

    F(0)=-2 D(exp(i pi/3))=-V,
    F''(0)=-sqrt(3).

The real derivative tends to -eta at the positive end and +eta at the
negative end. Thus Re F(t)<=-V-c|t| outside a compact interval. This gives
absolute convergence and uniform control of the noncompact tails.

For completeness, (R-i0) in (3.1) can first be any small negative horizontal
displacement. Between two strictly negative scaled heights in (-pi,0), the
same tail computation is uniform; the vertical ends of the deformation
vanish. This proves contour independence and then its prescribed lower
boundary value. No poles are crossed in moving to the chosen line.

On a small interval around zero, expand the holomorphic F to second order.
Its quadratic term is real and negative. Outside that interval the strict
maximum and linear tails give an exponentially smaller contribution. Scaling
t=b v and dominated convergence gives

    integral exp(F(t)/(2 pi b^2)) dt
       = exp(-V/(2 pi b^2)) (2 pi b)/3^(1/4) (1+o(1)).

The uniform O(b^2) quantum amplitude cannot change or cancel this nonzero
leading Gaussian term. Multiplying by 1/(2 pi b) proves (3.3). QED.

This is a fixed ideal geometric saddle, separated from the quantum poles by
a fixed gap in scaled coordinates. It is not the shrinking compact
tetrahedron fold in Section 11 of the user's manuscript. No uniform passage
through that fold has been used.

## 4. Exact quantum A-operator and minimality for the figure-eight state

Let I(x,y) be the integrand of (3.1), without the outside factor in (3.2).
Put Q_1=exp(-2 pi b x), Q_2=exp(-2 pi b y), and let E_1,E_2 shift x,y
downward by i b. From (2.6) and the elementary Gaussian shift,

    E_1 I=q Q_1^2 Q_2^(-2)(1+q^(-1/2)Q_1^(-1)Q_2) I,
    E_2 I=Q_1^(-2)(1+q^(1/2)Q_1^(-1)Q_2)^(-1)
                         (1+q^(-1/2)Q_2^(-1))^(-1) I.        (4.1)

This independently verifies the local input to the literature elimination.
Clearing denominators in the proper order gives exactly g_1,g_2 in the
v3 source. The explicit certificate

    q^(9/2) Q_1^2 P=q a_1 g_1-a_2 g_2

was independently expanded in the four-generator Ore algebra. The executable
certificate, including every coefficient, is
`experiments/audit_ore_certificate.py`; its residual is identically zero.

This check alone does not justify integrating shifts. To do that, first take
b sufficiently small, x in a small neighborhood of zero in the scaled
variable X=2 pi b x, and the contour used in Section 3. All the finitely many
shifts in P lie in a fixed smaller holomorphic strip. The action at X=0 has
strictly decaying linear tails, and these tails persist uniformly for small
complex X and small contour translations. Therefore vertical boundary terms
vanish. Integrating E_2^j I gives the same integral as I; E_1 can be brought
outside the integral. This proves

    P_q(E,Q,1) chi_b=0.

The shift of the outside factor in (3.2) is q times that factor. Consequently
the polynomial q P_q(q^(-1)E,Q,1) annihilates J_b. In normal order it is

    Ahat_q=a_2(Q) E^2+a_1(Q) E+a_0(Q),
    a_2=q^2 Q^2(q Q^2-1),
    a_1=-(q^2 Q^2-1)
          [q^4 Q^4-q^3 Q^3-q(q^2+1)Q^2-q Q+1],
    a_0=q^2 Q^2(q^3 Q^2-1).                                 (4.2)

The identity holds on the just-proved nonempty parameter domain. It extends
by analytic continuation wherever the same literature state and operators
are continued. This last wording is deliberate: a newly chosen contour after
crossing poles is not automatically the same continued state.

### 4.1 Minimality is a separate argument

We now prove that the state cannot have a rational first-order annihilator.
This avoids inferring minimality from the elimination output.

In scaled variables X=2 pi b x, u=2 pi b y the classical exponent numerator
for chi_b is

    S(X,u)=Li_2(-exp(X-u))-Li_2(-exp u)-X(2u-X).               (4.3)

The saddle at (X,u)=(0,-2 pi i/3) is nondegenerate. The implicit function
theorem gives a holomorphic saddle u(X) for small complex X. The gap at the
maximum, the linear tails, and the fixed strip gap in Section 3 persist in
a small complex neighborhood of X=0. Deform the contour a small amount to
pass through u(X). The same Gaussian argument, uniformly on compact subsets
of this neighborhood, proves a nonzero leading asymptotic and therefore

    J_b(x-i b)/J_b(x) -> ell(Q),    Q=exp(-X),                (4.4)
    ell=exp(-partial_X S(X,u(X))).

The prefactor exp(4 pi i c_b x) in (3.2) contributes q to this ratio and hence
does not change (4.4). The derivative of the saddle itself does not enter,
because partial_u S=0.

Put Y=exp(-u(X)). Exponentiating the critical equation and evaluating the
derivative in (4.4) gives

    Q Y^2+(Q^2+Q-1)Y+Q^2=0,
    ell=(Q^2+QY)/Y^2.

Eliminating Y, for Q^2!=1 and then by analytic continuation, gives

    Q^2 ell^2-F(Q) ell+Q^2=0,
    F(Q)=Q^4-Q^3-2Q^2-Q+1.                                 (4.5)

Its discriminant is

    F(Q)^2-4Q^4
      =(Q-1)^2(Q+1)^2(Q^2-3Q+1)(Q^2+Q+1),                  (4.6)

which is not a square in C(Q). The branch ell(Q) cannot be a rational
function, even though it is holomorphic locally at the complete point.

Suppose (r_1(Q,q)E+r_0(Q,q))J_b=0 with rational coefficients. Clear
denominators and remove their common vanishing power at q^(1/2)=1 (or q=1
when coefficients are rational in q). At least one specialized
coefficient at q=1 is nonzero. Taking (4.4) would give

    r_1(Q,1) ell(Q)+r_0(Q,1)=0,

contradicting (4.6). A nonzero order-zero annihilator is excluded by (3.3).
The coefficients in (4.2) have no common nonunit factor at generic q.
Thus (4.2), up to the declared Laurent units and a choice of sign, is the
primitive minimal-degree operator of Definition 5 for this state. This
argument is over the rational q-difference coefficient field; it does not
assert new Hilbert-space domain or all-level-N results.

### 4.2 The full classical peripheral factor

The exact specialization of (4.2) is

    Ahat_1=(Q^2-1)[Q^2 E^2-F(Q)E+Q^2].                      (4.7)

The primitive generic-q coefficients acquire a common factor only in the
classical limit. Dividing by Q^2-1 and then setting Q=1 is not the same
operation as specializing the full operator at Q=1. In particular this is a
concrete example of why the user's warning about peripheral factors matters.

The independently established volume statement is (3.4) for the state of this
minimal operator, with its normalization fixed by (3.1)–(3.2). It does not
assign a volume rate to every solution of (4.2).

## 5. A broad state-integral theorem, with explicit certificates

We now use the *existing* integral (4.5) of Ben Aribi–Wong, rather than choosing
a new positive integrand. The theorem below provides sufficient data that
can be checked without accepting their asymptotic proof.

Let X be an ordered ideal triangulation with N tetrahedra. To avoid confusing
the two pairs of matrices, write script-A, script-B for face matrices and
A,B for the N-by-N Neumann–Zagier matrices. Supply the following certificates:

1. script-A is invertible and the face construction gives a real symmetric
   Gaussian matrix Q_f. Let

       H=Q_f-diag((epsilon_j+1)/4),    G=-2H.

2. B is invertible and the finite identity G=B^(-1)A holds. This is the matrix
   identity in the literature FAMED definition.
3. Positive complete shapes z_j in the upper half plane, with compatible
   logarithms, satisfy

       A Log z+B Log z''=i nu,      nu in pi Z^N,

   and the remaining edge and meridian completeness equations. The tetrahedra
   are the actual geometric triangulation, so sum D(z_j)=Vol(M).
4. For the boundary coordinate of the literature integral, set

       p=2 B^(-1)e_N.

   Supply a rational constant gamma for which

       p^T(-Log z+i pi 1)=i pi gamma.                        (5.1)

   It can be checked directly at the geometric solution, or obtained from the
   symplectic peripheral certificate described below. Choose p_1!=0 by
   relabeling.

In this notation the literature integral at its complete boundary value is

    J_X(hbar,0)=C_X (2 pi sqrt(hbar))^(-N)
       integral exp((i y^T H y+c^T y)/(2 pi hbar))
                 product_j Phi_b(y_j/(2 pi sqrt(hbar)))
                 dy_2 ... dy_N,
    c=B^(-1)nu-G pi 1,
    y_1=(i pi gamma-sum_(j>=2) p_j y_j)/p_1.                (5.2)

Use the exact nonzero constant C_X of the chosen literature convention and
the horizontal contour through y*=-Log z+i pi 1. Its imaginary coordinates
all lie in (0,pi). Thus the source's angle structure can be chosen to be the
actual complete geometric angle structure.

**Normalization detail.** Equation (4.5) as printed has C_X=p_1/det(script-A).
The displayed preceding change of variables x=p^T y-i pi gamma has Jacobian
p_1, so directly disintegrating the full Lebesgue measure instead gives
1/(p_1 det(script-A)), with signs depending on orientation conventions.
This constant discrepancy needs reconciliation in an exact state comparison.
The subsequent `faddeev_pentagon_audit.md`, Section 7.1, makes the conversion
explicit: J_coarea=J_printed/p_1^2, with orientations fixed consistently.
This is also independent of which coordinate is eliminated when the coarea
fiber form is used.
For the complex identity with positive Lebesgue disintegration, the
orientation sign is sign(det(script-A)p_1). The full tensor phase and its
exact state-recovery formula are derived in `peripheral_phase_and_state.md`.
It is present also in the v2 TeX source, lines 3277–3292; it is not a PDF
extraction artifact.
The theorem uses the printed integral as its fixed definition; either explicit
nonzero constant has the same volume limit. No boundary-dependent or
exponentially significant factor is hidden in that observation.

**Theorem 5.1.** For the exact integral (5.2), with these certificates,

    lim_(b->0+) -2 pi hbar log|J_X(hbar,0)|=Vol(M).           (5.3)

The integral is nonzero for sufficiently small b. The conclusion is not
conditioned on a presumed asymptotic formula or absence of cancellations.

### 5.1 Finite identities and geometric saddle

The kinematical reduction requires no stationary phase: integrating
delta(script-A f+script-B t) in the face variables f gives

    K_X(t)=|det(script-A)|^(-1) exp(2 pi i t^T Q_f t).

The determinant follows from an ordinary invertible linear change of
variables. Formula (2.5) converts negative and positive tetrahedral factors
to the common product of Phi_b used in (5.2), with the explicit unit-modulus
constants retained when reconstructing the whole partition function. The
face identity G=B^(-1)A is a supplied finite matrix identity, not a consequence
of calling a triangulation geometric.
The subsequent `face_edge_stokes_identity.md` proves its edge rows for
every globally branched triangulation with an invertible face matrix;
the specified peripheral row and its completion remain separate requirements.
The subsequent peripheral-phase note explicitly reconstructs those constants
and the complete angle-dependent phase, rather than using the magnitude
formula as a state identity.

Condition (5.1) can be certified using rational matrices C,D with

    A D^T-B C^T=Id,
    B^(-1)A symmetric,
    2 e_N^T(C Log z+D Log z'')=H_m+i pi nu_m.

Indeed B^(-T)=D G-C, so at the complete gluing solution

    p^T y*=H_m+i pi nu_m
            -2 i e_N^T D B^(-1)nu
            +2 i pi e_N^T B^(-T)1.

Here H_m=0 by completeness and the other coefficients give gamma explicitly.
This reconstructs the step needed from the symplectic peripheral data. The
existence of particular C,D can be checked as part of the certificate; their
geometric interpretation is not inferred merely from invertibility of B.

The classical phase of (5.2) is

    F_0(y)=i y^T H y+c^T y-i sum_j Li_2(-exp y_j).

Its gradient is

    grad F_0=-i G y+c+i Log(1+exp y).

At y*=-Log z+i pi 1, Log(1+exp y*)=Log z''. Hence

    grad F_0(y*)=i B^(-1)(A Log z+B Log z'')+B^(-1)nu=0.     (5.4)

This is a full critical point before restricting to the boundary fiber.

For y=h+i d, direct use of the definition of the Bloch–Wigner function gives

    Re F_0(y)=h dot Re(grad F_0(y))+sum_j D(-exp y_j).

At y*, -exp y_j*=1/z_j, and D(1/z)=-D(z). Therefore

    Re F_0(y*)=-sum_j D(z_j)=-Vol(M).                        (5.5)

Only elementary identities of the dilogarithm and the checked gluing
equations enter this critical-value calculation.

### 5.2 A uniform bound, the hbar/b^2 distinction, and no cancellation

It would be incorrect to replace sqrt(hbar) by b inside Phi_b without
accounting for the error. Put s=b^2 and define the exact classical part

    F_s(y)=i y^T H y+c^T y
             -i/(1+s)^2 sum_j Li_2(-exp((1+s)y_j)).          (5.6)

Since hbar/b^2=(1+s)^(-2), (2.2) gives the exact integrand representation

    exp(F_s(y)/(2 pi hbar)) a_b(y),
    a_b(y)=exp(sum_j R_b((1+s)y_j)).                         (5.7)

On any horizontal fiber with all (1+s)Im y_j in a fixed compact subset of
(0,pi), a_b=1+O(s) uniformly over all its real directions.

Parametrize the boundary fiber by y=y*+T u, u in C^(N-1), where T is the
real, full-column-rank matrix implementing (5.2). On a horizontal contour its
real Hessian is

    Hess_u Re F_s
       = -T^T diag( Im[exp((1+s)y_j)/(1+exp((1+s)y_j))] ) T. (5.8)

Every diagonal entry inside the bracket is strictly positive, because
0<(1+s)Im y_j<pi. Hence (5.8) is negative definite at every finite real
point. At s=0, the complex Hessian restricted to the fiber is invertible:
its Hermitian real part is negative definite. The holomorphic implicit
function theorem therefore gives a critical point u_s=O(s) of the restricted
F_s. The contour can be translated a small complex amount to u_s+R^(N-1);
all imaginary coordinates keep a fixed strip gap.

Here are the global bounds needed for this translation and for Gaussian
asymptotics. On the translated contour, Re F_s has zero gradient at its
critical point and is strictly concave everywhere. On the unit ball its
negative Hessian has a uniform positive lower bound for sufficiently small s.
Along any outward ray concavity makes the radial derivative nonincreasing.
Consequently there is c>0, independent of small s, such that

    Re F_s(y_s+T v)
       <= Re F_s(y_s)-c min(|v|^2,|v|),  v in R^(N-1).      (5.9)

The same linear tail bound, with adjusted constants, holds during the small
contour translation. The quantum amplitude is uniformly bounded by (5.7).
Thus all boundary faces at infinity vanish in the contour deformation, and
the noncompact tails are uniformly negligible in stationary phase.

The Gaussian matrix has negative definite real part. Its Gaussian integral
is nonzero, with the square root of its determinant fixed by continuation
from real negative definite matrices. Equations (5.7)–(5.9) therefore give

    J_X(hbar,0)
      = C_X/(2 pi sqrt(hbar))
          exp(F_s(y_s)/(2 pi hbar))
          /sqrt(det(-Hess_u F_s(y_s))) (1+o(1)).             (5.10)

In particular a cancellation between unrelated saddles has not been assumed
away: the contour has a unique strict maximum, its local Gaussian is nonzero,
and the rest is exponentially smaller. Since F_s(y_s)->F_0(y*) and hbar tends
to zero, (5.5) and (5.10) prove (5.3). QED.

The N=1 case, if applicable, is a zero-dimensional fiber and follows directly
from (5.7); the determinant and Gaussian integration are then omitted.

### 5.3 What this proves about a broad knot class

For every knot exterior with a supplied positive geometric FAMED
triangulation and compatible peripheral certificates, the published integral
(4.5) has the volume law (5.3), by the above argument. The theorem does not
depend on a claimed census computation or a claimed proof that a family has
these certificates. Such membership claims need their own verification.

The subsequent twist-family note supplies uniform face, angle and geometric
certificates for the explicit literature families. Its
[topological companion](twist_topology_and_peripherals.md) reconstructs the
diagrammatic identification with the named twist knots and independently
identifies the meridian and preferred longitude, including their branches.
General two-bridge and alternating families are not yet covered by those
formulas.
Menasco's checkerboard polyhedra provide combinatorics; their existence alone
does not supply the positive shape solution and matrix identity in items
1–4. A claim that they are actual all-right-angled cells of the complete
metric requires additional hypotheses.

Theorem 5.1 is a theorem about the specified literature *state integral*.
The subsequent note `general_annihilator_and_volume.md` supplies a finite
dimension-count and exponential-moment proof of annihilator existence in the
Andersen–Malusà b-shift algebra for these rescaled integrals, as well as their
classical geometric component. The canonical knot-state identification and
the different finite-b operators of the FAMED paper remain separate questions.
`twist_family_audit.md` supplies uniform geometric and matrix formulas for the
two explicit twist face families; the topological companion identifies those
families and their peripheral rows. Invariance of the whole state under
all triangulation changes, including the correct boundary factors, also
requires its own exact identities.

## 6. Reproducible diagnostics

Run

    python3 experiments/audit_ore_certificate.py
    python3 experiments/check_literature_state_volume.py

The first is an exact polynomial computation. The second evaluates the
convergent remainder (2.3), checks (2.6) at several points, and evaluates the
full quantum integrand on the contour in (3.5). For b=0.5,0.35,0.25,0.18,0.12,
the scaled state exp(V/(2 pi b^2)) J_b(0) is approximately

    0.6786085741, 0.7155266487, 0.7356954991,
    0.7468279065, 0.7539044805,

approaching 3^(-1/4)=0.7598356857. Changing Gaussian quadrature order from
128 to 256 changes the reported answers by at most 2e-11. These diagnostics
support the calculations; the bounds and proofs above carry the conclusions.
