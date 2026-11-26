# Global injectivity of positive marked logarithmic gluing

Research proof, 22 November 2026.

Positive ideal shapes give a global uniqueness statement for a fixed
logarithmic gluing system. The proof compares two configurations in the
product of shape strips; their joining segment need not satisfy any
gluing equation. It also proves that the inverse is holomorphic on the
realized image. No existence or source-cycle assertion is included.

## 1. The positive shape coordinates and the real constraint matrix

Let
\[
 \mathcal S=\{x\in\mathbb C:0<\operatorname{Im}x<\pi\},
 \qquad z=e^x,
 \qquad v(x)=-\operatorname{Log}(1-e^x).                 \tag{1}
\]
The logarithm in (1) is principal. Since \(z\) is in the upper
half-plane, \(1-z\) is in the lower half-plane, so this defines one
holomorphic function on the entire convex strip. In particular,
\[
 0<\operatorname{Im}v(x)<\pi,\qquad
 v'(x)=\frac{e^x}{1-e^x},\qquad
 \operatorname{Im}v'(x)
       =\frac{\operatorname{Im}(e^x)}{|1-e^x|^2}>0.       \tag{2}
\]
For \(t\ge1\), apply \(v\) separately to the coordinates of
\(x\in\mathcal S^t\). Let \(A,B\) be real \(t\)-by-\(t\) matrices
satisfying
\[
 R=(A\ B),\qquad \operatorname{rank}R=t,
 \qquad AB^{\mathsf T}=BA^{\mathsf T}.                  \tag{3}
\]
Define the holomorphic logarithmic constraint map
\[
                  F_R(x)=Ax+Bv(x).                    \tag{4}
\]
Neither block in (3) is required to be invertible.

Use the complex bilinear alternating form
\[
 \Omega((a,b),(c,d))=a^{\mathsf T}d-b^{\mathsf T}c
                       \quad\text{on }\mathbb C^{2t}.   \tag{5}
\]
The real kernel of \(R\) is Lagrangian for this form. Indeed it is
the image of the rank-\(t\) matrix
\(\binom{-B^{\mathsf T}}{A^{\mathsf T}}\): multiplication by \(R\)
gives zero, and the pairing of two of its columns is zero by (3).
Its complexification is therefore isotropic and is closed under
complex conjugation.

## 2. A strict comparison for any two positive configurations

For \(x,x'\in\mathcal S^t\), write
\(\Delta x=x-x'\) and \(\Delta v=v(x)-v(x')\).
Convexity of the strip and the fundamental theorem of calculus give
\[
 \Delta v_j=\Delta x_j\int_0^1
                   v'(x'_j+s\Delta x_j)\,ds.           \tag{6}
\]
Consequently
\[
 \operatorname{Im}\sum_j\overline{\Delta x_j}\Delta v_j
   =\sum_j|\Delta x_j|^2
       \int_0^1\operatorname{Im}v'(x'_j+s\Delta x_j)\,ds
   >0\quad\text{if }x\ne x'.                          \tag{7}
\]
The points of the segment in (6) are used only to evaluate the
one-variable function (1). No gluing condition is imposed there.

**Theorem.** Under (3), \(F_R\) is injective on \(\mathcal S^t\).
Its complex Jacobian is invertible everywhere. Hence it is a
biholomorphism onto the open realized image \(F_R(\mathcal S^t)\).

Suppose first that \(F_R(x)=F_R(x')\). Then
\(w=(\Delta x,\Delta v)\) and \(\overline w\) lie in the
complexification of the real Lagrangian kernel in Section 1. Thus
\[
 0=\Omega(\overline w,w)
       =2\mathrm i\operatorname{Im}
                         \sum_j\overline{\Delta x_j}\Delta v_j.
                                                               \tag{8}
\]
By (7), this forces \(x=x'\), proving injectivity.

At any point the complex Jacobian is
\[
             J_R(x)=A+B\operatorname{diag}(v'(x_j)).    \tag{9}
\]
If \(J_R(x)a=0\), the vector
\(w=(a,\operatorname{diag}(v'(x_j))a)\) belongs to the same
complexified Lagrangian kernel. Its pairing with its conjugate is
\[
 0=\Omega(\overline w,w)
             =2\mathrm i\sum_j\operatorname{Im}v'(x_j)|a_j|^2.
                                                              \tag{10}
\]
Equation (2) forces \(a=0\). This proves (9) is invertible.
The holomorphic inverse-function theorem supplies local inverses;
injectivity makes them agree on every overlap. Their union is the
single holomorphic inverse on the realized image. This proves all
assertions of the theorem.

## 3. Actual edge rows and arbitrary primitive filling directions

Consider an actual oriented ideal triangulation with \(t\)
tetrahedra and \(c\) torus ideal-vertex links, with positively ordered
shapes. Retain every face identification, edge occurrence and marked
primitive peripheral path. In the convention (1), the incidence
argument in [M] gives \(t-c\) independent real edge rows. Their
peripheral symplectic quotient has dimension \(2c\); different cusps
pair to zero, and each cusp's primitive meridian and longitude have
nonzero intersection pairing.

Append one row
\[
                 \gamma_i=a_i\mu_i+b_i\lambda_i,
       \qquad (a_i,b_i)\in\mathbb R^2\setminus\{(0,0)\}, 
                                                              \tag{11}
\]
at each cusp. These rows are independent modulo the edge rows and
pair to zero. The complete \(t\)-row system therefore satisfies
(3), as proved locally in [M]. This rank and isotropy argument is
incidence-theoretic and does not depend on the shape values.
For integral coprime \((a_i,b_i)\), (11) is the original primitive
path; real coefficients give the corresponding real polarization.

Fix the actual affine logarithmic target, including all edge
windings, peripheral signs, and constants introduced by the quad
convention. The equations are then precisely
\[
                         F_R(x)=q.                   \tag{12}
\]
The theorem gives at most one positive assignment satisfying this
fixed target, across all positive components, and a nonsingular
Jacobian at every such assignment. No completeness hypothesis is
needed for this uniqueness and transversality step.

In particular one may keep a meridian row at every unfilled cusp
and choose \(\mu_i+p_i\lambda_i\) at every designated filled cusp,
with arbitrary fixed real \(p_i\). Mixed signs and \(p_i=0\) cause
no exception. For an actual integral filling the similarity-log
equation has its prescribed primitive target, for example
\[
                       U_i+p_iV_i=-2\pi\mathrm i.       \tag{13}
\]
The logs in (13) are the actual continued similarity logs, with
their original primitive basis. They are not uncentered SL eigenlogs
or equations only modulo \(2\pi\mathrm i\).

Deleting dependent edge rows does not lose constraints: their linear
relations and constants must agree in the full marked system. If
they did not agree, that target would have no solution. Quad changes
likewise transform both the rows and their affine constants. The
theorem does not compare different logarithmic lifts of one
exponentiated equation.

One useful consequence concerns continuation along the same fixed
primitive slopes, with the right sides of (13) varying continuously.
No two positive solutions at a fixed target can collide, and no
Jacobian can become singular at an interior positive point. A
continuation remaining in a compact subset of \(\mathcal S^t\)
extends past a finite endpoint by compactness and (9). This does not
prove that such compact containment or continuation exists.

## 4. Algebraic multipliers at a realized target

Suppose now that \(A,B\) have integer entries and that all
\(\gamma_i=e^{q_i}\) are nonzero algebraic numbers. Exponentiating
(12) gives the square rational system
\[
 G_i(z):=\prod_j z_j^{A_{ij}}(1-z_j)^{-B_{ij}}
                               =\gamma_i,\quad 1\le i\le t.   \tag{14}
\]
Work on \(\prod_jz_j(1-z_j)\ne0\). At a realized positive solution,
\[
 D_zG=\operatorname{diag}(\gamma_i)J_R(x)
                                  \operatorname{diag}(z_j^{-1})
                                                              \tag{15}
\]
is invertible. Thus this is an isolated nonsingular algebraic
solution and all its shapes are algebraic. Here is also a direct
field argument. Over a number field containing the \(\gamma_i\),
differentiate (14) in the finitely generated field generated by the
\(z_j\). Equation (15) forces every \(dz_j\) to vanish. In
characteristic zero the dimension of these differentials is the
transcendence degree, so that field is a finite algebraic extension.

Other positive solutions of (14) can have different logarithmic
targets \(q+2\pi\mathrm i k\). They are not identified by this
corollary. Global uniqueness is the fixed-log statement (12).

## 5. Relation to the earlier results and the remaining boundary

[M] proves the all-cusp marked incidence and local polarized
Jacobian theorem. [E] proves global comparison, fixed-slope
uniqueness and positive-region elimination for its explicit original
eight-tetrahedron edge blocks. The argument (6)--(10) gives a global
comparison directly in the product of ideal-shape strips, for any
real Lagrangian constraint matrix. It does not require the original
wire or peripheral image to be convex. Polarized rigidity and
geometric variational principles are established subjects; no
historical novelty claim is made here.

Uniqueness does not supply a positive point. Already for \(t=1\),
\(A=1,B=-1\), the target \(q=-\log8\) would imply
\(z(1-z)=1/8\), whose two roots are real. There is no positive
solution. Nor is the realized image asserted convex or the map to
\(\mathbb C^t\) asserted proper. A hyperbolic filling need not be represented by a
positive assignment on this same fixed triangulation and log lift.

The result does not construct a cone path, prove primitive metric
completion from multiplier equations, identify a quantum source
critical scheme, or select the coefficient of its original cycle.
The original closing, normal data, and noncancellation estimates
remain separate. No finite-exception or volume-limit theorem follows.

## Complete proof sources

* M: [Marked multicusp rigidity](../papers/marked-fillings/README.md),
  261 lines, SHA-256
  f882d2c7d1f723590391d3cc03dcd9bba7a12d13c2e006c6dea570e1b4af1b42.
* E: [Positive edge global monotonicity](research_positive_edge_global_monotonicity.md),
  678 lines, SHA-256
  da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500.
