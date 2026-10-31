# Actual cleared cross cofactors: interior starting-row packet

The [whole-source local packet](general_full_spectral_numerator_geometric_packet.md) now assembles these results for the actual full numerator. The original global spectral filling period remains open.

31 October 2026. Internally reviewed. This concerns the
original finite homogeneous cofactor, not an arbitrary interpolation of
its complete-channel samples. The middle face b is positive. The separate
protected-middle proof treats b=0. Exactly one protected outer face x=0
or y=0 is included below; both outer faces zero are excluded.

## 1. The finite determinant and the exact physical-node adapter

Use the original level N, theta=pi/N, h=1/N, and put

  alpha_j(u)=4cos^2((j+1/2)theta)+u,
  s_j=2sin(j theta), A=x+y, P=xy,
  p_j=s_j^2 A, q_j=s_j s_(j-1)alpha_(j-1)(u)P.

Let $A_{[0,j]}(u)$ be the original upper two-diagonal matrix with diagonal
alpha_r, entries -p_r at (r-1,r), and -s_r s_(r-1)P at (r-2,r).
The absent physical entries are zero. The actual cleared cofactor is

\[
R_j(b,u)=\det A_{[0,j]}(u)\,(1,b,\ldots,b^j)\,
                      A_{[0,j]}(u)^{-1}e_j. \tag{1}
\]

Equivalently, replace the LAST ROW of A_[0..j] by (1,b,...,b^j) and
take its determinant. Row replacement proves (1) off the poles; the
determinant proves its polynomial extension across every alpha_r=0.
Thus it is not necessary to assume an invertible physical block.

The exact path formula is

  R_j= sum_(i=0)^j b^i [prod_(r<i)alpha_r] K_(i,j),       (2)
  K_(i,i)=1, K_(i,i-1)=0,
  K_(i,v)=p_v K_(i,v-1)+q_v K_(i,v-2).

Consequently R_0=1 and

  R_j=b^j prod_(r<j)alpha_r+p_j R_(j-1)+q_j R_(j-2).     (3)

There is a precise link to the previous positive q-Hahn determinant,
but only at its actual spectral node. Write a_r=alpha_r(0), and fix
0<=a<=floor((N-1)/2). At u=-a_a, alpha_a=0, so for j>=a,

  R_j(b,-a_a)=K_(a,j)(-a_a) R_a(b,-a_a),
  R_a(b,-a_a)=S_(2a) D_a(x,b,y).                         (4)

For the second identity use the original full-numerator value at that
node: the all-CROSS formula equals N^2 times the literal complete-circle
polynomial, including its beta and forced factors. The first identity
makes its b and c dependence R_a(b)R_a(c). Comparing the monic b^a,c^a
coefficients with the original D_a(b)D_a(c) gives (4), since

  prod_(r<a)(a_r-a_a)
   =prod_(r<a)4sin((a+r+1)theta)sin((a-r)theta)=S_(2a).

The scalar outer factor is a nonzero polynomial (already nonzero at
x>0,y=0), so cancellation takes place in the polynomial domain. The
odd simple node is included. The case a=0 is the empty product1.
Equation (4) does NOT identify generic-u R_j with a moving-dimensional
q-Hahn determinant. Formula (1) is its actual off-node continuation.

## 2. Statement of the relative complex packet

Fix a compact positive real set with b>0, A>0 and x,y>=0. A zero outer
face stays exactly zero; other faces vary in a small fixed complex
logarithmic neighborhood. Let the terminal row n=n_N satisfy

  n/N=1/2+O(1/N),  n<=floor(N/2),

as for R_(m-2), R_(m-1) and the odd R_m. The constants in the O term
are bounded. For all sufficiently large N there are holomorphic phases
phi_N(t;u,x,b,y) and holomorphic units a_N(t;u,x,y), on a fixed complex
neighborhood of the interior real starting saddle, such that

  R_n(b,u)=sqrt(2pi N) a_N(t_N)
       exp[N phi_N(t_N)]/sqrt(-partial_t^2 phi_N(t_N))
       *[1+O(N^-1)].                                    (5)

Here t_N is the unique nearby zero of partial_t phi_N, and the square
root is continued from its positive real value at u=0. All finite
prefix products and the actual terminal n remain in phi_N; no source
scalar is discarded. The estimate is uniform on a sufficiently small
FIXED complex u disk and the indicated face neighborhood, with fixed
parameter derivatives on smaller neighborhoods. In particular R_n is
a unit there for all sufficiently large N.

The phases converge with fixed derivatives to

  phi(t;u)=t Log b+integral_0^t Log alpha(v,u)dv
                    +integral_t^(1/2) Log lambda(v,u)dv,
  alpha(v,u)=4cos^2(pi v)+u,
  lambda(v,u)=2sin(pi v)[sin(pi v)A
             +sqrt(sin^2(pi v)(x-y)^2+(4+u)P)].          (6)

The square root and logarithms are continued from positive real values
where their respective integrals occur. Only alpha on [0,t] is logged;
it is uniformly nonzero there. Zeros of alpha near the UPPER terminal
do not enter that logarithm or cause a zero of lambda. The limiting
saddle is the analytic continuation of

  sin^2(pi t_b(u))=(1+u/4)b^2/[(b+x)(b+y)],
  t_b(0) in (0,1/2).                                   (7)

For x=0 this is (1+u/4)b/(b+y), and similarly for y=0.
At u=0 the critical value in (6) is the original absolute triangle
potential F(x,b,y). The finite terminal shift is retained in phi_N,
not replaced by1/2 in the prefactor or finite action.

## 3. Uniform analytic dominant tail, including zero upper diagonals

Choose fixed 0<ell<t_b(0)<r<1/2 uniformly over the real compact, with
the saddle separated from ell,r. On a larger real interval containing
[ell,1/2], the transfer recurrence for K has

  p(t)=4sin^2(pi t)A,
  q(t,h)=4sin(pi t)sin(pi(t-h))
                       [4cos^2(pi(t-h/2))+u]P.

At h=u=0 the two characteristic roots are lambda and lambda_-, with
lambda a unit and |lambda_-/lambda|<=kappa<1. This remains true in a
fixed small complex t/face/u neighborhood and for small h. It includes
the terminal alpha=0 cases: only the smaller root may vanish. If P=0,
q=0 and the recurrence is first order, with the same unit dominant root.

An exponentially accurate analytic ratio can be constructed directly.
Start from the analytic positive characteristic root of z^2-pz-q=0,
and iterate

  r_(l+1)(t)=p(t)+q(t,h)/r_l(t-h).                      (8)

Use nested rectangles whose left real margin advances by h at each
step; keep one extra shifted rectangle for the final residual. On a
uniform O(h) neighborhood of the starting root, (8) preserves that
neighborhood and has pointwise derivative modulus at most kappa'<1.
Translation of the analytic seed costs O(h). After L=floor(cN) steps,
where c is smaller than the available left margin, r_N is analytic,
a unit, and

  r_N(t)-p(t)-q(t,h)/r_N(t-h)=O(exp(-c_1 N)),
  r_N(t)=lambda(t,u)+O(h).                             (9)

The contraction estimate is between successive nested rectangles, not
an assumed contraction on a fixed domain invariant under translation.
Cauchy estimates on the retained common neighborhood give all fixed
derivative bounds. The construction never divides by lambda_-.

For integer i/N in [ell,r], divide the actual K_(i,j) by
Y_j=prod_(v=i+1)^j r_N(vh), with Y_i=1. In the exact zero-residual
recurrence, consecutive differences of K/Y multiply by

  -k_N(jh), k_N(t)=q(t,h)/[r_N(t)r_N(t-h)], |k_N|<=kappa'.

The initial values are K_(i,i)=1,K_(i,i-1)=0. Hence the dominant initial
projection is the analytic truncated sum

  a_N(t)=sum_(l=0)^(L') (-1)^l prod_(v=1)^l k_N(t+vh), (10)

with L'=floor(c_2 N) smaller than every remaining terminal distance.
The omitted tail is exponential. Its leading value is
1/(1+k_0(t)), a positive unit, and a_N differs from it by O(h).
The residual (9) adds O(N exp(-c_1 N)) to the normalized solution:
the difference recurrence and a geometric-series bound control the
solution uniformly, then a discrete Gronwall factor is1+o(1).
Thus uniformly in all these actual integer starts and complex parameters,

  K_(i,n)=a_N(ih) prod_(v=i+1)^n r_N(vh)
                         [1+O(exp(-c_3 N))].          (11)

## 4. Exponentially accurate analytic starting-row interpolation

On [0,r] and its fixed complex neighborhood, alpha(t+h/2,u) is an
analytic unit. The midpoint prefix product prod_(v<i)alpha_v can
therefore be interpolated by an optimally truncated Euler--Maclaurin
primitive, anchored at0. The tail product in (11) has the same
construction applied to Log r_N, anchored at the ACTUAL t=n/N.
Uniform holomorphy gives C^k k! derivative bounds. Choosing the number
of Bernoulli terms proportional to N gives an O(exp(-c_4 N)) remainder
on smaller fixed neighborhoods, as in the proved analytic discrete
primitive lemma for the original fold factors.

Explicitly, on a retained analytic strip of width d_0, the order-2K
Euler--Maclaurin remainder for a log SUM is bounded by

  C h^(2K-1) (2K)!/(2pi d_0)^(2K)
       <= C h^(-1) [C_0 K h]^(2K).

The same estimate holds for the midpoint rule, whose periodic Bernoulli
functions have the same factorial bound. It follows from the integral
remainder and |f^(2K)|<=C (2K)! d_0^(-2K); the strip and C are uniform
for both Log alpha and the constructed Log r_N. Choose
K=floor(c_0/h) with C_0 c_0<1. The polynomial h^(-1) is absorbed by
shrinking the positive exponential constant. Thus the LOG-product
error, and hence its relative product error, is O(exp(-c_4 N)),
uniformly in the actual integer endpoints. The finite truncated
primitive itself is holomorphic on the smaller strip used below.

Keep these finite primitives, rather than only their leading integrals.
With the exact b^i factor and (10), they define

  w_N(t)=a_N(t) exp[N phi_N(t)]

such that EACH actual summand of (2), for i/N in [ell,r], equals
w_N(i/N)[1+O(exp(-c_5 N))]. The phase converges with fixed derivatives
to (6). All primitive anchors, their endpoint half terms and finite
terminal shifts stay in phi_N. This proves the normalization claim in
(5), without inferring a continuum phase solely from node interpolation.

All starts OUTSIDE [ell,r], including i=0, remain in the argument.
At positive faces and u=0 the uniform interval theorem gives their
exact weighted rate. The limiting phase is strictly maximized at
t_b(0), since its derivative is Log[b/L(t;x,y)] and L is strictly
increasing from0 to infinity. Choose ell,r so those tails have a fixed
gap c_6>0, uniformly over the real compact.

For small complex u, apply the ORIGINAL unused-row product bound to
each term in (2). The product of all nonzero lower-row ratios is at
most exp[N theta(|u|)+O(log N)], theta(v)=arcosh(1+v/2).
This also covers odd terminal n=m: the cofactor excludes alpha_m=0.
The original missing steps and all other starting rows are retained.
A small logarithmic face perturbation costs exp(C rho N), since each
term has the same finite homogeneous degree n. Taking the fixed u and
face neighborhoods small enough makes their total cost less than
c_6 N/4. The entire omitted starting-row sum is therefore exponentially
below the continued saddle, not merely small at a real parameter.

## 5. The actual discrete saddle and its contour

At u=0, partial_t^2 phi(t)<0 uniformly on [ell,r]. On a sufficiently
small fixed complex parameter neighborhood, the IFT gives a holomorphic
t_N with partial_t phi_N(t_N)=0, t_N=t_b(u)+O(1/N), and
Re[-partial_t^2 phi_N] bounded below by a positive constant near the
continued horizontal saddle contour.

The finite-grid replacement is justified, including its vertical edges.
Let ell_N,r_N^end be the half-grid boundaries around the integer starts
in [ell,r]. For a fixed small height eta, the exact residue formula is

  sum_i w_N(i/N)
    =N/(2i) integral_(rectangle) cot(pi N z) w_N(z) dz. (12)

On the upper/lower sides cot(pi N z)=-/+ i+O(exp(-2pi eta N)).
On the vertical half-grid sides its modulus is at most1. The real
endpoint gap persists along those sides for small eta and small complex
parameters. On the horizontal sides the phase costs at most C eta^2
at the real reference, plus C rho from the parameter perturbation.
Choose eta first so 2pi eta>C eta^2, then rho small enough for the
cotangent error and vertical currents to have a uniform exponential
gap relative to exp[N phi_N(t_N)]. Cauchy's theorem now compares (12)
with N times the ordinary integral along [ell_N,r_N^end]; the retained
vertical connector terms have the same gap. No endpoint current has
been declared identically zero.

The exponentially small interpolation error from section4 also stays
exponentially small AFTER summation: its possible absolute-sum loss is
O(rho N), and the parameter neighborhood was chosen smaller than its
fixed exponential accuracy. Deform the ordinary interval to the
horizontal segment through t_N, retaining both endpoint connectors.
Uniform strict concavity along that segment gives the Gaussian formula
(5), with relative O(N^-1) and the continued positive square root.
Analyticity and Cauchy margins give the claimed fixed parameter
derivatives of that relative error.

## 6. What this packet does and does not supply

The proof treats b>0 and every actual starting row; i=0 is exponentially
subdominant in this chart. It includes x=0 or y=0, where q=0, (8) is
exact, and a_N=1. It does NOT discard i=0 when b itself is the protected
zero: that different chart is the separate protected-middle theorem.

Under u=-4sin^2(pi delta), the packet is holomorphic in delta on a fixed
small cover neighborhood. In particular it covers selected fixed
delta=O(1/n_twist) sectors once the signed twists are sufficiently long
for this fixed diagram. This is a finite cofactor asymptotic, not a
choice of a contributing charge or cycle in the full Gaussian period.
The exact central cross formulas must still be assembled with their
literal alpha prefactors, both parities and original shared coefficient
extraction. Their leading central factors are nonzero near u=0, but
the whole phase-sensitive period requires its own selection argument.

Once the separate b=0 packet and the exact central factors are included,
there is a direct calibration of the local LEADING action. At every
physical fold node, the all-cross polynomial is exactly N^2 B_(N,a).
These nodes become dense in a fixed small real delta interval. Uniform
convergence of the present normalized logarithm and the already proved
complete fold interpolation therefore gives

  psi_b(u(delta))+psi_c(u(delta))
       =F(x,b,y)+F(x,c,y)-V(delta;x,b,c,y),

where psi_b=phi(t_b(u);u). The real node values are positive, fixing the
logarithmic branch and absolute constant. Both sides are holomorphic,
so the identity extends to the same small complex cover neighborhood,
with shared-face derivatives. This identifies a leading local action;
it does not identify the finite cofactor with the old interpolant or
prove a global face-torus gap or selected Gaussian contribution.

## Focused finite validation

Private helper ../experiments/audit_actual_cross_cofactor_interior_packet.py compares the
row-replaced determinant directly with the cleared recurrence and compares
its physical-node values with the independently built ORIGINAL positive
q-Hahn matrices. At 85 digits, N=3,...,18, real/complex faces and each
one-protected-outer specialization, it passes1056 row determinants,
352 matrix node adapters,352 exact sine scalars and960 tail factorizations;
maximum relative error is below2e-85. These checks validate the finite
adapter. The relative complex asymptotic is the analytical proof above,
not a conclusion inferred from finite node or rate samples.

## Independent review

Root, coherent_partner_currents and conway_reduced_geometry independently reviewed the full analytical packet proof: PASS. Root also checked the explicit optimal Euler--Maclaurin remainder. The focused finite adapter audit is separately scoped above. Stable private proof; no whole face-torus or Gaussian-cycle claim is made here.

[Focused audit](../experiments/audit_actual_cross_cofactor_interior_packet.py) · [Recorded output](../experiments/actual_cross_cofactor_interior_packet_results.json). These finite checks supplement the written proof and retain the scope recorded in their output.
