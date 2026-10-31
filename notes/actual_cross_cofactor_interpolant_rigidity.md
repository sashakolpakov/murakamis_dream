# Actual all-CROSS cofactors and the complete-fold interpolant

The [whole-source local packet](general_full_spectral_numerator_geometric_packet.md) now assembles these results for the actual full numerator. The original global spectral filling period remains open.

31 October 2026. Internally reviewed. This is a
quantitative analytic consequence of the reviewed actual cofactor packets.
It does not infer a generic-q derivative or select a Gaussian cycle.
All face zeros remain the ORIGINAL protected zeros.

## 1. Exact objects and the theorem

Let P_(N,cross)(u;l) be the original local all-CROSS numerator, with the
sign (-1)^d already included, and let mathcal B_N(delta;l) be the EXACTLY
anchored interpolation in actual_positive_face_exponential_fold_interpolation.md.
Thus

 u(delta)=-4sin^2(pi delta),
 delta_a=(N-1-2a)/(2N),
 P_(N,cross)(u(delta_a);l)=N^2 B_(N,a)(l),                (1)
 B_(N,a)/mathcal B_N(delta_a)=1+O(exp(-cN)).             (2)

Both P_(N,cross)(u(delta)) and mathcal B_N(delta) are even in delta.
Equation (1) is the original paired/simple-node identity with its actual
N^2 factor. Equation (2) keeps the original B_(N,M) anchor, half-index,
forced factor, beta factors and complex face neighborhood.

Fix a compact positive geometric face set in any one of its actual
protected-zero patterns. The reviewed ordinary-middle and protected-middle
cofactor packets imply that, after decreasing a FIXED disk and FIXED
complex face neighborhood, there is kappa>0 such that

 P_(N,cross)(u(delta);l)
       =N^2 mathcal B_N(delta;l)[1+O(exp(-kappa N))]     (3)

uniformly for |delta|<=a and l in that neighborhood, for both parities
and all sufficiently large N. All fixed delta and face derivatives of
the relative error obey the same statement on smaller neighborhoods.
The positive number a is independent of N. It may depend on the fixed
diagram/face compact and the previously proved analytic accuracy.

This theorem concerns the ACTUAL finite cofactor, not a freely chosen
interpolation of its nodal values. The proof uses its independent complex
packet to control its off-node growth. No uniqueness assertion is made
for arbitrary analytic functions having the same physical node values.

## 2. The whole central factor is an analytic unit

Write A=x+y, P=xy, m=floor(N/2), D_b=R_(m-1)(b,u),
E_b=(a_(m-1)+u)R_(m-2)(b,u), and G_b=R_m(b,u) at odd levels.
Put

 S=sqrt(A^2+uP), Lambda_*=2(A+S),                      (4)

with S=A at u=0. The actual cofactor packets, including their finite
terminal rows, imply uniformly on a fixed complex neighborhood

 R_n/R_(n-1) -> Lambda_*,

for the terminal rows used here. For b>0 this follows from the same
starting-row saddle with one more terminal recurrence step; the
inhomogeneous terminal source is exponentially smaller because its
start is separated from the strict interior saddle. For b=0 it is the
explicit protected-middle packet. When P=0 it follows from the exact
first-order terminal recurrence. No division by a vanishing smaller
transfer eigenvalue is used.

The exact even factorization gives

 P_cross/(D_b D_c)
   =s_m^2 A+s_m s_(m-1)P(E_b/D_b+E_c/D_c)
       ->4A+8uP/Lambda_*=4S.                          (5)

The exact odd factorization gives

 P_cross/(G_b G_c)
    =1+u s_m s_(m+1)P D_b D_c/(G_b G_c)
       ->1+4uP/Lambda_*^2=2S/(A+S).                 (6)

Both limits are holomorphic units near u=0, also at one-outer-zero
specializations. Equations (5),(6) retain the actual finite coefficients;
they are used here only to establish a uniform nonvanishing factor and
its subexponential logarithmic size. Thus the full local P_cross has a
holomorphic logarithm on a fixed small disk and complex face polydisc.
Its normalized logarithm converges there, uniformly on smaller closures,
to the sum of the two actual cofactor actions.

## 3. Subexponential ratio growth, with no fitted normalization

The same uniform normalized-log convergence holds for mathcal B_N from
its original B_(N,M) anchor and the explicit analytic fold interpolation.
At positive real faces and sufficiently small real delta, every cofactor
packet above is on its positive branch; hence all logarithms can be
chosen real there. The dense physical nodes (1),(2) force the two
limiting normalized logarithms to agree on that real delta interval.
The identity theorem extends the equality in delta and then in each
complex face variable. Equivalently one may use the independently
proved absolute cofactor/complete-action identity; it fixes the same
constant and is not needed as an extra interpolation assumption.

Consequently, on one fixed outer circle |delta|=R and a smaller fixed
closed face neighborhood,

 sup |P_cross/(N^2 mathcal B_N)| <= exp(o(N)),
 sup |P_cross/(N^2 mathcal B_N)-1| <= exp(o(N)),        (7)

where o(N)/N tends to zero uniformly. The exact N^2 contributes only
2log N to a logarithm. No uncontrolled face-dependent exponential
normalization is introduced. A polynomial bound would suffice but is
not necessary; the uniform subexponential estimate (7) is enough.

## 4. Finite Cauchy--Lagrange rigidity, including both parity grids

Set f_N(delta)=P_cross/(N^2 mathcal B_N)-1. On a fixed real interval
|delta|<=a, take EVERY physical node and its reflection. At odd N this
is the grid j/N (including0); at even N it is (j+1/2)/N. Thus the chosen
nodes t_0<...<t_(M-1) have spacing exactly1/N, lie in [-a,a], and

 M=2aN+O(1),     |f_N(t_j)|<=C exp(-cN).              (8)

Evenness supplies the negative nodes without a new continuation or
phase convention. Choose 0<a<R/8 within the original physical matching
window, and evaluate |z|<=a. The exact interpolation formula is

 f_N(z)=sum_j f_N(t_j) ell_j(z)
   +(1/(2pi i)) integral_(|zeta|=R)
       f_N(zeta)/(zeta-z)
           product_j[(z-t_j)/(zeta-t_j)] dzeta.        (9)

There are no other poles since mathcal B_N is a unit on the outer disk.
The contour remainder is at most

 C exp(o(N)) [2a/(R-a)]^M.                            (10)

Its exponent is strictly negative, uniformly in the fixed complex face
parameters. To bound the noisy-node polynomial, use the exact spacing:

 product_(k!=j)|t_j-t_k|
       =N^(-(M-1)) j! (M-1-j)!,
 sum_j |ell_j(z)|
       <= (4aN)^(M-1)/(M-1)!
       <= exp([2a log(3e)+o(1)]N).                   (11)

The harmless 3e accommodates the bounded endpoint rounding. Choose a
still smaller so 2a log(3e)<c/2. Equations (8),(11) then give an
exponentially small polynomial part. Equations (10),(11) prove (3),
with some fixed kappa>0. Analytic Cauchy estimates on nested disks and
face neighborhoods give all fixed derivative versions. Since both sides
are even, they also define the same exponentially accurate relative
comparison in the spectral coordinate u near0, on a smaller fixed disk.

## 5. Consequences and remaining estimates

The old complete-fold interpolation now describes the actual all-CROSS
local numerator, including its spectral derivatives, with exponential
precision. This is stronger than matching only the principal phase or
only the original node values. The semisimple nodal ambiguity is resolved
HERE by the independent actual cofactor growth theorem and (9), not by
formally differentiating an arbitrary root identity.

For finitely many original ports the local relative comparisons multiply
on the common positive-face complex chart, with the same kind of
exponential error. The original shared target and physical half-powers,
cups, mark and finite phase scalars must still be retained. In particular
(3) by itself does not identify an entire shared face-torus coefficient:
its angular complement needs an actual uniform estimate. Nor does it
prove the selected full Gaussian contour, the surviving charge sum, or
a genuine-q first-normal theorem. No external-color alias is discarded.

Validation is analytical: (1) has its independently reviewed original
source audit; (2) is the frozen exponential interpolation theorem; the
ordinary/protected cofactor packets have separate full proof reviews.
The Cauchy--Lagrange step is an exact finite formula and is proved above,
not inferred from numerical agreement at increasingly dense nodes.

## Independent review

Root and coherent_partner_currents independently reviewed the full analytical proof: PASS, including the central factors, uniform subexponential quotient, both physical grids and the exact noisy-node Cauchy--Lagrange estimates. Stable private proof; no numerical audit is substituted for this analytic corollary.
