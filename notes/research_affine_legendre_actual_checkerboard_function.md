# Affine Legendre duality for the actual checkerboard factorial function

Private written proof, 19 November 2026.

The checkerboard source has an exact reciprocal-factorial function of
affine logarithms. Its Gaussian and linear terms are fixed by the
original finite source. This note identifies that function and proves
the appropriate Legendre theorem for an injective rectangular system
of logarithms. The radial minimum is a constrained maximum of positive
tetrahedron volumes. Positivity of the shape arguments alone does not
imply that the constraint is feasible.

For the actual five-factor alternating closed-braid function below,
the displayed zero-character constraint is never strictly feasible: an exterior-strand
circulation lies on a support face throughout its positive-shape
chamber. Thus this exact rewrite cannot by itself supply a finite
positive critical point for that marked potential. Retained nonzero
Fourier characters require their own test. The obstruction uses the original source
quadratic, not a generic warning about contour selection.

The finite source cycle is retained as its original finite sum of
residue circles. No equality with the Legendre chain is asserted.
The complete directs are C, the actual checkerboard source, and F,
the exactly normalized factorial. The convex duality and all source
Gaussian calculations used below are proved inline.

## 1. A rectangular positive factorial potential

Let \(A\) be a real \(m\)-by-\(r\) matrix of rank \(r\), let
\(H=H^{\mathsf T}\) be real, and let \(a\in\mathbb R^m\) and
\(\kappa\in\mathbb R^r\). Use the marked potential
\[
 W(x)=\sum_{j=1}^m\operatorname{Li}_2(e^{\ell_j(x)})
       +\tfrac12x^{\mathsf T}Hx+i\kappa^{\mathsf T}x+c,
 \qquad \ell(x)=Ax+ia,\qquad c\in\mathbb R.
 \tag{1}
\]
On the chamber below, each dilogarithm has its upper-half-plane
mark. Write \(x=\rho+i\theta\) and
\[
 \alpha=A\theta+a,\quad b(\theta)=-H\theta-\kappa,
 \quad Z_\alpha=A^{\mathsf T}\prod_{j=1}^m[0,\pi-\alpha_j].
 \tag{2}
\]
The relevant domain is the strictly feasible projection
\[
 \Omega=\{\theta:0<\alpha<\pi,\quad
       \exists\,0<\beta<\pi-\alpha,
                     \ A^{\mathsf T}\beta=b(\theta)\}.
 \tag{3}
\]
It may be empty. If nonempty, it is a bounded open convex polytope:
it is a linear projection of strict linear inequalities and equalities;
\(\operatorname{rank}A=r\) bounds \(\theta\) when \(A\theta+a\) is bounded.
The strict image of the box is exactly the interior of \(Z_\alpha\).
Indeed a surjective linear map is open. Conversely fix an interior
box point with image b_0. For any interior image point b and small
positive epsilon, \((b-\epsilon b_0)/(1-\epsilon)\) still belongs
to the image. A preimage of that point, mixed with weight epsilon
with the fixed interior box point, is an interior preimage of b.
The image is full dimensional because A has rank r.

**Affine Legendre theorem.** For every \(\theta\in\Omega\),
\(F(\rho,\theta)=\operatorname{Im}W(\rho+i\theta)\) has a unique
proper radial minimum \(\rho_L(\theta)\). It is real analytic.
With \(\gamma=\pi\mathbf1-\alpha-\beta\), its value is exactly
\[
 V_{\rm eff}(\theta)=
 \max_{\substack{\beta,\gamma\ge0\\
       \beta+\gamma=\pi\mathbf1-\alpha\\
       A^{\mathsf T}\beta=b(\theta)}}
       \sum_{j=1}^m
       [\Lambda(\alpha_j)+\Lambda(\beta_j)+\Lambda(\gamma_j)],
 \qquad
 \Lambda(t)=-\int_0^t\log(2\sin s)\,ds.
 \tag{4}
\]
The maximizer is unique and strictly positive. Its radii satisfy
\[
 A\rho_L=\log\frac{\sin\beta}{\sin\gamma},\qquad
 \beta_j=-\operatorname{Arg}(1-e^{(A\rho_L)_j+i\alpha_j}).
 \tag{5}
\]
The graph \(x_L=\rho_L+i\theta\) has nonzero complex Jacobian
everywhere. Its effective volume has negative definite Hessian.

## 2. Coercivity, the fiber maximum, and the Hessian

For \(0<\alpha_j<\pi\), put
\(f_j(t)=\operatorname{Im}\operatorname{Li}_2(e^{t+i\alpha_j})\).
Then
\[
 f_j'(t)=-\operatorname{Arg}(1-e^{t+i\alpha_j})\in(0,\pi-\alpha_j),
 \qquad
 f_j''(t)=\operatorname{Im}\frac{e^{t+i\alpha_j}}
                                      {1-e^{t+i\alpha_j}}>0.
 \tag{6}
\]
Its limits are \(f_j(t)\to0\) at \(-\infty\) and
\(f_j(t)-(\pi-\alpha_j)t\to0\) at \(+\infty\), obtained
from the marked dilogarithm derivative and continuation. For the
second limit use
\(\operatorname{Li}_2(z)+\operatorname{Li}_2(z^{-1})
=-\pi^2/6-\operatorname{Log}(-z)^2/2\), where
\(\operatorname{Log}(-z)=t+i(\alpha_j-\pi)\) for upper z.
Consequently
\(f_j(t)-(\pi-\alpha_j)\max(t,0)\) is bounded on the real line.
In particular
\[
 F(\rho,\theta)=\sum_j f_j((A\rho)_j)-b(\theta)\cdot\rho,
 \quad
 F_\infty(v)=\sum_j(\pi-\alpha_j)\max((Av)_j,0)-b\cdot v.
 \tag{7}
\]
The second expression is the support function of \(Z_\alpha\)
minus \(b\cdot v\). It is strictly positive for every nonzero v
exactly when b is in its interior. In that case its minimum on the
unit sphere is positive, and (7) proves linear coercivity of F.
Its radial Hessian is positive definite by rank A and (6), proving
existence and uniqueness. If b is outside the zonotope, F tends to
minus infinity on a ray. On its boundary a supporting ray has finite
limiting F by the displayed limits of the f_j, so proper coercivity
fails. Thus the interior condition is necessary as well as sufficient.

For fixed alpha, the summand in (4) has beta derivative
\(-\log(\sin\beta_j/\sin\gamma_j)\) and second derivative
\[
       -\cot\beta_j-\cot\gamma_j
       =-\frac{\sin\alpha_j}{\sin\beta_j\sin\gamma_j}<0.
 \tag{8}
\]
The closed fiber is compact. Any boundary candidate can be joined to
a strictly feasible point. Every vanishing beta or gamma then gives
a positive infinite one-sided derivative of volume, while the other
terms have finite derivatives. Thus a maximum is interior, and (8)
makes it unique. Its constrained derivative says that
\(\log(\sin\beta/\sin\gamma)\in\operatorname{im}A\), giving
a unique rho. The ordinary sine rule proves (5). The identity
\[
 f_j((A\rho)_j)-(A\rho)_j\beta_j
       =\Lambda(\alpha_j)+\Lambda(\beta_j)+\Lambda(\gamma_j)
 \tag{9}
\]
is the Bloch--Wigner identity on this marked positive shape. It also
follows by differentiating both sides in beta using (8), and fixing
the value at beta=0. Summing (9) and using \(A^{\mathsf T}\beta=b\)
proves (4). This is the same minimizer as (7), not a separately
chosen positive angle point.

Let \(H_W=W_{xx}=K+iD\) along the graph. Direct differentiation gives
\[
 D=A^{\mathsf T}\operatorname{diag}_j
                  \operatorname{Im}\frac{z_j}{1-z_j}A>0,
 \quad
 K=H+A^{\mathsf T}\operatorname{diag}_j
                  \operatorname{Re}\frac{z_j}{1-z_j}A,
 \quad z_j=e^{\ell_j(x_L)}.
 \tag{10}
\]
The real Hessian of F is \(\left[\begin{smallmatrix}D&K\\K&-D\end{smallmatrix}\right]\).
The implicit function theorem and radial critical equation give
\[
 R=\partial_\theta\rho_L=-D^{-1}K,\qquad
 \operatorname{Hess}V_{\rm eff}=-D-KD^{-1}K<0,
 \quad J_L=R+iI=-D^{-1}\overline{H_W}.
 \tag{11}
\]
The matrix \(H_W\) is invertible since its imaginary part is positive
definite. Hence \(\det J_L\ne0\). These statements hold on the whole
feasible domain, not only at a critical point.

Suppose now a marked critical point \(x_*\) of W is supplied in this
positive chamber. Its imaginary equation is precisely (3), and its
real equation is
\(H\rho_*=A^{\mathsf T}\log|1-z_*|\). On the complete angle
polytope in (3), the differential of total volume at this point is
\[
 -\log|1-z_*|\cdot A\,d\theta-(A\rho_*)\cdot d\beta
       =-\rho_*^{\mathsf T}(H\,d\theta+A^{\mathsf T}d\beta)=0.
 \tag{12}
\]
For one tetrahedron, the negative two-angle volume Hessian has
diagonals \(\cot\alpha+\cot\gamma>0\) and
\(\cot\beta+\cot\gamma>0\), off-diagonal \(\cot\gamma\), and
determinant one. It is positive definite. This strict concavity,
and injectivity of the joint coordinates \((\theta,\beta)\), make
this the unique maximum of that compact angle polytope. Equivalently
it is the unique maximum of (4). No identification of its value
with a knot volume is made without an actual gluing identification.

For any compact convex \(P\Subset\Omega\) with \(\theta_*\) inside,
the radial homotopy
\[
 x_s(\theta)=(1-s)\rho_*+s\rho_L(\theta)+i\theta
 \tag{13}
\]
has a strict uniform boundary gap. Indeed \(F(\rho_*,\theta)\)
has Hessian \(-D<0\) on its convex positive chamber and a critical
point at theta_*. The effective volume has the same maximum by (11).
Radial convexity bounds F on (13) by their convex combination.
On the compact boundary of P both maxima have a strict loss.

## 3. The exact checkerboard source function

Use C's actual connected alternating closed-braid diagram, with
\(c\ge1\) crossings and its fixed integer face gauge. Its face
coordinate vector v has dimension \(r=c+1\). Write the integer
linear charges as \(u_j(v),z_j(v),A_j(v),B_j(v)\), with
\(u_j+z_j=A_j+B_j\). The exact cap is \(L_j=d-u_j-z_j\).
Let \(w=c_0v/N\), \(c_0=2\pi i\), and denote the corresponding
linear forms in w by U_j,Z_j,A_j,B_j. Thus, for example,
\(U_j(c_0v/N)=c_0u_j(v)/N\). Set
\[
 S_j=U_j+Z_j,\qquad \ell_{j,L}=c_0-S_j.
 \tag{14}
\]
The latter is the marked logarithm for the index \(L_j+1\), not L_j.
Retain the original pivot as
\(q^{-2\tau_N(w)}\), where \(\tau_N(w)=\tau_{\rm piv}(Nw/c_0)\)
uses C's complete affine expression, including every d-dependent
constant.

Define the real-quadratic/pure-imaginary-linear polynomial
\[
 Q_*(w)=\sum_j\left\{
 \tfrac34U_j^2+\tfrac12U_jZ_j+\tfrac34Z_j^2
 +\tfrac{\sigma_j}{4}(Z_j-U_j)(B_j-A_j)
 -\tfrac{c_0(3+\sigma_j)}4 S_j\right\}.
 \tag{15}
\]
With exactly F's normalized \(\widehat F_N\), put
\[
 \begin{split}
 a_N(w)&=q^{-2\tau_N(w)}
     \prod_j e^{(3+\sigma_j)S_j/4}(1-e^{-S_j}),\\
 \mathcal I_N(w)&=
 \frac{a_N(w)e^{NQ_*(w)/c_0}}
 {\prod_j\widehat F_N(NU_j/c_0)^2
          \widehat F_N(NZ_j/c_0)^2
          \widehat F_N(N\ell_{j,L}/c_0)} .
 \end{split}
 \tag{16}
\]
At every allowed original integer face state this is EXACTLY
\[
 \mathcal I_N(c_0v/N)=
 q^{\frac12\sum_j\sigma_j[(z_j-u_j)(B_j-A_j)-d(u_j+z_j)]
                                  -2\tau_{\rm piv}(v)}
       \prod_j(S_{u_j}^2S_{z_j}^2S_{L_j})^{-1},
 \tag{17}
\]
where the capital S factorials on the right have C's meaning.
Consequently the original scalar is still
\[
 K_N=\chi_N\kappa^{\mathrm{wr}}(x_0/s)^{b-1}N^{2c-1}
              \sum_{v\in\mathcal F_N}\mathcal I_N(c_0v/N),
 \qquad x_0=-q^{-1},\quad s=x_0^N .
 \tag{18}
\]
Here \(\mathrm{wr}=\sum_j\sigma_j\) is the original writhe of C.

Here is a direct check of all marks in (16). For any original index n,
\[
 S_n^{-1}=e^{c_0n(n+1)/(4N)-c_0n/4}/\widehat F_N(n).
 \tag{19}
\]
For U=c_0n/N the exponent is
\(N(U^2/4-c_0U/4)/c_0+U/4\).
For the last index write \(n=L+1\). Its exponent instead is
\(N(\ell_L^2/4-c_0\ell_L/4)/c_0-\ell_L/4+c_0/4\).
The exact functional equation supplies
\[
 \widehat F_N(n-1)^{-1}
                   =(1-e^{\ell_L})\widehat F_N(n)^{-1}.
 \tag{20}
\]
At n=N the quotient is interpreted by its removable value
\(\widehat F_N(N-1)^{-1}\); no endpoint is deleted.
Adding the two U copies, two Z copies and last copy in (19) gives
the first three quadratic terms of (15), the linear term
\(-3c_0S/4\), and the amplitude \(e^{3S/4}(1-e^{-S})\).
Finally C's exact clock chirp contributes its quadratic in (15),
\(-c_0\sigma S/4\), and \(e^{\sigma S/4}\) because d=N-1.
The pivot is untouched. This proves (16)--(18), including their
extensive constants and subleading characters.

## 4. Its affine positive chamber and the exact analytic gate

The shape-positive chamber for this SAME function is
\[
 0<\operatorname{Im}U_j<\pi,\quad
 0<\operatorname{Im}Z_j<\pi,\quad
 \pi<\operatorname{Im}(U_j+Z_j)<2\pi .
 \tag{21}
\]
Its five logarithmic rows per crossing are U,U,Z,Z,c_0-U-Z.
They have real coefficients and pure imaginary offsets, including
the retained offset \(2\pi\) in the last row. Their matrix A is
injective: if all U and Z charges vanish, all dual-edge increments
vanish, and C's fixed face gauge forces every coordinate to vanish.
The real quadratic and imaginary linear pieces of (15) therefore
fit (1). F's exact uniform expansion on any compact subset of (21)
gives the actual potential
\[
 W_*(w)=\sum_j\{2\operatorname{Li}_2(e^{U_j})
       +2\operatorname{Li}_2(e^{Z_j})
       +\operatorname{Li}_2(e^{-S_j})-5\operatorname{Li}_2(1)\}
                       +Q_*(w).
 \tag{22}
\]
The real constant \(-5c\operatorname{Li}_2(1)\) is fixed, not reset.
The marked logarithm in the last dilogarithm is still c_0-S, whose
imaginary part is in (0,pi); using -S as its logarithm in the
Gaussian part would change the source.

More precisely, on that compact set
\[
 \mathcal I_N(w)=N^{-5c/2}e^{NW_*(w)/c_0}
             \bigl(a_0(w)B(w)+O(N^{-1})\bigr),\quad
 B(w)=\prod_j[i(1-e^{U_j})]^{-1}
                   [i(1-e^{Z_j})]^{-1}
                   [i(1-e^{-S_j})]^{-1/2} .
 \tag{23}
\]
All square roots are F's right-half-plane marks. The factor a_0 is
the nonzero holomorphic limit of a_N. Indeed
\(\tau_{\rm piv}(v)=t^{\mathsf T}v+d t_0\) with integral t,t_0,
so its exact exponential in (16) is
\(e^{-t^{\mathsf T}w}e^{c_0t_0/N}\). Thus the error and every
fixed derivative are uniform on smaller buffers. No arbitrary
factorial interpolation or unknown periodic multiplier is used.

The theorem of Sections 1--2 applies only on the subset of (21)
where the source's own target \(-H\theta-\kappa\), read from
(15), lies in the indicated open zonotope. Neither (21) nor the
existence of five positive arguments proves this condition. In
particular the quadratic in (15) cannot be discarded or replaced
by a preferred gluing quadratic. Likewise a critical point of
(22) must be identified with the intended geometric point using
the actual source and peripheral equations.

For any affine factorial function satisfying strict feasibility and
possessing a marked critical point, Sections 1--2 and F's compact
expansion give a compact Legendre chain with a nonzero Gaussian
coefficient and its calibrated radial comparison. With m factorial
rows in r variables, its unnormalized period has power
\(N^{-(m+r)/2}\), its actual amplitude times \(\det J_L\), and the
accretive determinant
\(\det(-J_L^{\mathsf T}W_{xx}J_L/c_0)^{1/2}\).
The next section shows why this conditional construction does NOT
apply to (22) on (21), despite its exact reciprocal-factorial form.

## 5. An exact exterior-strand support face

Assume (21) is nonempty; otherwise there is nothing to test. Denote
its angles by \(\theta_U,\theta_Z\) and
\(\theta_S=\theta_U+\theta_Z\). For a real face-coordinate
direction h, write \(h_U,h_Z,h_A,h_B\) for its charge increments.
The support function of the five-row zonotope in that direction is
the sum over crossings of
\[
 2(\pi-\theta_U)(h_U)_+
 +2(\pi-\theta_Z)(h_Z)_+
 +(\theta_S-\pi)(-h_U-h_Z)_+.
 \tag{24}
\]
Its support gap from the prescribed source target is
\(\mathfrak g_\theta(h)=\operatorname{supp}Z_\alpha(h)-b\cdot h\).
Thus one adds to (24) the directional value of
\(H\theta+\kappa\), with H and kappa fixed by (15).

There is a nonzero honest flow h with this gap exactly zero for
EVERY theta in (21). To construct it, use the outer braid position1.
Connectedness and c>=1 imply that generator sigma1 occurs: otherwise
the closed first strand would be a separate crossing-free component.
List these occurrences cyclically in braid height, closing along the
actual first closure arc. Position1 is untouched between occurrences.
At a positive occurrence its outer output is under and its outer
input is over; at a negative occurrence these roles are reversed.
Alternation along the intervening edge therefore forces consecutive
occurrences to have the same sign. All sigma1 occurrences have one
sign \(\varepsilon\).

If epsilon is positive, set h_u=1 at precisely those occurrences and
all other h_u,h_z=0. The outer edge from an under-output to the next
over-input says that the permutation a cycles exactly this set.
Consequently its four increments are
\[
       (h_U,h_Z,h_A,h_B)=(1,0,1,0)
       \quad\hbox{on the exterior occurrences},
 \tag{25}
\]
and zero elsewhere. If epsilon is negative, set h_z=-1 there and
all other increments zero. The outer edge from an over-output to
the next under-input makes b cycle that set, giving
\[
       (h_U,h_Z,h_A,h_B)=(0,-1,0,-1).
 \tag{26}
\]
Both are nonzero real integer flow directions. C's integral face
coordinate bijection supplies their actual h after the fixed gauge.

Here is the full local support calculation, including the source
quadratic. In (25), the sine-factorial quadratic terms and the source linear
term in (15), added to (24), give
\((\theta_Z-\theta_U)/2\). The chirp gives
\((\theta_A-\theta_B-\theta_Z+\theta_U)/4\).
Using \(\theta_A+\theta_B=\theta_U+\theta_Z\), their sum is
\[
           \mathfrak g_j=(\theta_A-\theta_U)/2.
 \tag{27}
\]
In (26), the corresponding two contributions are
\((\theta_U-\theta_Z)/2\) and
\((\theta_B-\theta_A+\theta_Z-\theta_U)/4\), giving
\[
           \mathfrak g_j=(\theta_B-\theta_Z)/2.
 \tag{28}
\]
All other rows contribute zero. Equations (27),(28) telescope around
the actual a-cycle or b-cycle of exterior occurrences. Thus
\(\mathfrak g_\theta(h)=0\) for a nonzero h. The target b cannot
be in the interior of its zonotope. In particular the domain (3)
is EMPTY for this five-factor source potential on chamber (21).

There is also a direct finite-radius consequence. The shape beta
vector at any finite rho is strictly inside its box. Since Ah is
nonzero, its support inequality in direction h is strict. Hence
\[
 \partial_h F(\rho,\theta)
       =(A^{\mathsf T}\beta-b)\cdot h<0.
 \tag{29}
\]
Along \(\rho+t h\), every changing shape reaches the corresponding
endpoint of that box exponentially as t tends to infinity. The
support gap is zero, so (7) shows that F has a finite limit on this
ray, and (29) tends to zero. This is a retained radial escape face,
not a finite critical point or a proper minimum. In particular the
displayed marked W_* has no critical point anywhere in (21).
A retained finite-sum Fourier character instead gives
\(W_*+c_0 n^{\mathsf T}w\), with its marked integral n, and shifts
the support target to \(b-2\pi n\). Its exterior support gap is
\(2\pi n\cdot h\), so (29) is not a test of all such characters.
Neither a nonzero character in this same shape chamber nor a
different positive polarization is excluded by this proof.

There is an explicit necessary character condition. The circulation
h is primitive integral because one of its edge increments is 1 or
-1. Let I be its set of exterior occurrences, all of sign epsilon.
The width of the zonotope in that direction is
\(\sum_{j\in I}[\pi+\varepsilon(\theta_{Z_j}-\theta_{U_j})]\),
as follows by adding the positive and negative supports in (24).
Testing both h and -h therefore requires
\[
 0<2\pi n\cdot h<
       \sum_{j\in I}[\pi+\varepsilon
                       (\theta_{Z_j}-\theta_{U_j})].
 \tag{30}
\]
At the uniform one-third angles this is \(0<n\cdot h<|I|/2\).
These are tests of retained integral characters, not assertions
that a character passing them occurs with nonzero source coefficient.

These are statements about the principal potential F, not finite-N
vanishing. The exact amplitude, shifted last factorial, pivot and
d=N-1 characters in (16) remain. They can affect a radial endpoint
layer when its distance grows with N; no uniform estimate of that
layer or cancellation of the original finite sum follows from (29).

## 6. The original cycle is a separate datum

Equation (18) retains the entire capped lattice and original scalar.
Equivalently it is the sum of small product residue circles around
those same integer face states, with one ordinary cotangent factor
of residue one per integer coordinate, applied to
\(\mathcal I_N(c_0v/N)\). At any removable endpoint use (20).
This is an exact representation of the same finite sum, including
all possible boundary and alias currents under a later deformation.

The exact function (16) removes an ambiguity about which scalar
function is being transformed. The affine Legendre theorem supplies
a precise necessary-and-sufficient feasibility test, and Section5
shows that its displayed zero-character five-factor potential fails
it. A candidate geometric branch must therefore retain and test
the appropriate nonzero character, or use a different actual
polarization or source transformation. No allowed character is
discarded by this test. Neither a
geometric cycle coefficient nor a new volume-conjecture case is
proved. The original cycle and its possible escape-face currents
remain in (18); the failed positive chamber is not discarded from
the finite source by a volume estimate.

## Complete directs

* C: notes/research_alternating_charged_checkerboard_polarization.md,
  435 lines, SHA256
  c7102909f30c008e45a8e7040a225f1de4164187709c5548ff316d49954f1098.
* F: notes/exact_factorial_interpolation_and_complex_contours.md,
  226 lines, SHA256
  1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72.

Both complete directs were freshly read nontruncated in this active
author/review sequence and retained unchanged. All proof steps above
are written mathematics; frozen and public files remain unchanged.
