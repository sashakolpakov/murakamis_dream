# Positive radial height contraction and its exact action cost

Private written proof, 16 November 2026.

In the original angle sector \(|\Re t_v|\le\pi/2\), simultaneously
contracting every imaginary angle to zero preserves all original
positive edge blocks. Heights may have either sign. Applied to the
actual inverse-period graph, this supplies the positivity hypothesis
needed by the previously proved vertical action-cost identity. The
result is an ascending homotopy to the real projection, not a
lower-action connector or a completed dual integration cycle.

## 1. Original coordinates and the contraction

Fix a finite original circle tree and a selected vertex set \(S\).
Include every edge incident to \(S\) once, and keep all outside
angles complete, \(t_b=0\). Every selected vertex has an incidence.
Write
\[
 t_v=s_v+i h_v,\qquad s_v,h_v\in\mathbb R,\qquad
 |s_v|\le\pi/2.
 \tag{1}
\]
At each edge \(e=vw\) put
\[
 a_v=\tan(t_v/2),\qquad a_w=\tan(t_w/2),\qquad
 q_e^2=1+a_v^2+a_w^2.
 \tag{2}
\]
Use the original positive branch, for which \(q_e(0,0)=1\).
The pinned positive-edge theorem identifies positivity of all
eight original tetrahedra with
\[
             \Re q_e>
                  \sqrt{(\Re a_v)^2+(\Re a_w)^2}.
 \tag{3}
\]
It also fixes the complete logarithmic returns
\[
 r_{v,e}=\operatorname{arsinh}
                  \bigl(\tan(t_v/2)\cos(t_w/2)\bigr),
 \qquad |\Im r_{v,e}|<\pi/2,
 \tag{4}
\]
with the corresponding endpoint-swapped formula. The branch in
(4) is the globally specified positive branch, rather than an
independent inverse-hyperbolic-sine choice at each point.

**Theorem 1 (height contraction).** Suppose every edge at (1) is
positive. Then every edge remains positive along
\[
                 t_v(\lambda)=s_v+i\lambda h_v,
                   \qquad 0\le\lambda\le1.
 \tag{5}
\]
All original square roots, face coordinates and return logarithms
continue on their canonical positive branches along (5).
No common sign of the heights or real angles is required.

**Proof.** The assertion is edgewise. Set
\[
 S_v=\sin s_v,\quad C_v=\cos s_v\ge0,\quad
 D_v(\lambda)=C_v+\cosh(\lambda h_v)>0,
 \tag{6}
\]
and likewise at \(w\). The exact tangent formula is
\[
 \Re a_v(\lambda)=\frac{S_v}{D_v(\lambda)},\qquad
 \Im a_v(\lambda)=\frac{\sinh(\lambda h_v)}{D_v(\lambda)}.
 \tag{7}
\]
For \(X=(\Re a_v)^2+(\Re a_w)^2>0\), the positive-edge
criterion (3) is equivalent to
\[
 \bigl(\Re a_v\Im a_w-\Re a_w\Im a_v\bigr)^2<X.
 \tag{8}
\]
This equivalence includes existence of the principal root with
positive real part: the strict inequality excludes a nonpositive
real discriminant, as proved in the pinned source.

If at least one of \(S_v,S_w\) is nonzero, then \(X>0\) for
every \(\lambda\). Multiplying the difference between the right
and left sides of (8) by \(D_v^2D_w^2\) gives exactly
\[
\begin{split}
 F(\lambda)={}&
 S_v^2\{1+C_w^2+2C_w\cosh(\lambda h_w)\}\\
 &+S_w^2\{1+C_v^2+2C_v\cosh(\lambda h_v)\}\\
 &+2S_vS_w\sinh(\lambda h_v)\sinh(\lambda h_w).
\end{split}
 \tag{9}
\]
Thus positivity is equivalent to \(F(\lambda)>0\).
If precisely one sine is zero, its surviving squared-sine term
is strictly positive for all \(\lambda\). If both are nonzero
and the last term is nonnegative, the same conclusion follows
from the positive constant terms.

It remains to treat a negative last term. Put
\[
 p=|S_v|>0,\quad q=|S_w|>0,\quad
 \alpha=|h_v|>0,\quad\beta=|h_w|>0,\quad L=\alpha+\beta.
 \tag{10}
\]
The sign of each nonzero \(\sinh(\lambda h)\) is fixed for
\(\lambda>0\). The hyperbolic product identity rewrites (9) as
\[
\begin{split}
 F(\lambda)={}&K+2p^2C_w\cosh(\beta\lambda)
                 +2q^2C_v\cosh(\alpha\lambda)\\
             &+pq\cosh((\alpha-\beta)\lambda)
                 -pq\cosh(L\lambda),\\
 K={}&p^2(1+C_w^2)+q^2(1+C_v^2)>0.
\end{split}
 \tag{11}
\]
For \(0\le k\le L\), the ratio
\[
                  \frac{\cosh(k\lambda)}{\cosh(L\lambda)}
 \tag{12}
\]
is nonincreasing on \(\lambda\ge0\). Its logarithmic derivative
is \(k\tanh(k\lambda)-L\tanh(L\lambda)\le0\), since
\(x\mapsto x\tanh(x\lambda)\) is nondecreasing on \(x\ge0\).
All nonconstant ratios in \(F(\lambda)/\cosh(L\lambda)\)
have nonnegative coefficients and frequencies in \([0,L]\);
the last term is the constant \(-pq\). Therefore
\[
 \frac{F(\lambda)}{\cosh(L\lambda)}
          \ge\frac{F(1)}{\cosh L}>0
                   \qquad(0\le\lambda\le1).
 \tag{13}
\]
This proves every case with \(X>0\), including \(C_v=0\) or
\(C_w=0\), so the closed real-angle sector in (1) is allowed.

Finally, if both sines vanish, (1) forces \(s_v=s_w=0\).
Both tangents are purely imaginary. The other case of the
positive-edge criterion is exactly
\[
 \tanh^2(\lambda h_v/2)+\tanh^2(\lambda h_w/2)<1.
 \tag{14}
\]
Each summand is nondecreasing in \(\lambda\ge0\); its strict
validity at \(\lambda=1\) implies validity on the full interval.
This completes the positivity proof.

Along (5), the angles remain in the original strip
\(|\Re t|<\pi\). Positivity keeps the principal \(q_e\) in the
right half-plane and all original face denominators nonzero.
The pinned positive disk/strip coordinates give the unique
complete return logarithms on this domain. At \(\lambda=0\)
all angles are real; scaling these real angles to zero keeps
every edge positive. Thus continuation along (5) uses the
same complete marking, with no integer shift or phase reset.
\(\square\)

Theorem 1 is a radial height statement. It does not assert
convexity of the entire positive domain in the angle variables,
nor independent contraction of the different heights.

## 2. Exact ascent from the inverse-period graph

Fix real powers \(n_v\) and real charges \(c_v\), with the
original integral convention \(n_v=\eta_v-2p_v\) when applicable.
Keep the primitive period and charged phase
\[
 \begin{aligned}
 P_v(t)&=\sum_{e\ni v}r_{v,e}(t)-\frac{i n_v}{2}t_v,\\
 \Phi_c(t)&=\sum_e\psi(t_v,t_w)
       +\frac{i}{4\pi}\sum_{v\in S}n_vt_v^2
       -i\sum_{v\in S}c_vt_v,\\
 (\Phi_c)_t&=-\frac{P+\pi i c}{\pi},\qquad
 J(t)=\frac{\partial P}{\partial t}.
 \end{aligned}
 \tag{15}
\]
Here \(\psi_t=-r_{v,e}/\pi\) is the original marked edge action.
The positive-edge theorem gives the symmetric Jacobian
\[
                         \Re J(t)>0
 \tag{16}
\]
on the selected coordinates: each selected vertex has an
incidence, and the real powers contribute only an imaginary
diagonal term.

**Theorem 2 (ascending action).** Suppose the point in Theorem 1
also lies on the actual inverse-period slice
\[
                          P(s+i h)=u-\pi i c,\qquad
                                    u\in\mathbb R^S.
 \tag{17}
\]
For \(g(\lambda)=\Re\Phi_c(s+i\lambda h)\), one has
\[
 \begin{aligned}
 g'(1)&=0,\\
 g''(\lambda)&=\frac1\pi
           h^{\mathsf T}\Re J(s+i\lambda h)h,\\
 g(\lambda)-g(1)&=\frac1\pi\int_\lambda^1
        (r-\lambda)\,
        h^{\mathsf T}\Re J(s+i r h)h\,dr.
 \end{aligned}
 \tag{18}
\]
If \(h\ne0\), the action strictly increases as \(\lambda\)
decreases from \(1\) to \(0\).

**Proof.** Theorem 1 supplies the entire positive segment
required for differentiating the canonical phase.
At \(\lambda=1\), (15)--(17) give
\(g'(1)=\Re(-i u^{\mathsf T}h/\pi)=0\).
Since \(t'(\lambda)=ih\) and \(t''(\lambda)=0\), the second
formula follows directly from \(\Phi_{tt}=-J/\pi\).
Twice integrating backward from \(\lambda=1\) gives the last
formula. Equation (16) makes \(g''>0\) if \(h\ne0\), and then
\(g'(\lambda)<0\) for every \(\lambda<1\).
\(\square\)

This applies to inverse-period points with arbitrary real \(u\),
not only to a critical point \(u=0\). The contraction generally
leaves the fixed imaginary-period slice as soon as \(\lambda<1\);
it does not keep the primitive equations fixed along the path.

There is a precise compact uniform version. Let \(K\) be a
compact family of positive points satisfying (1), with the same
finite graph and fixed powers. Its image under (5) is a compact
subset of the open positive domain, by Theorem 1 and continuity.
Consequently there are \(0<\mu_K\le\Lambda_K<\infty\) such that
\[
 \mu_K I\le\Re J(s+i\lambda h)\le\Lambda_K I
           \quad(t=s+ih\in K,\ 0\le\lambda\le1).
 \tag{19}
\]
For those points of \(K\) satisfying (17), (18) gives
\[
 \frac{\mu_K}{2\pi}(1-\lambda)^2|h|^2
 \le g(\lambda)-g(1)
 \le\frac{\Lambda_K}{2\pi}(1-\lambda)^2|h|^2.
 \tag{20}
\]
A uniform strictly positive gap requires both
\(1-\lambda\) and \(|h|\) bounded away from zero; compactness
alone does not impose that additional condition.

For a compact part of the original inverse-period graph
\(t(s)=s+i h(s)\) contained in this sector, (5) gives the
explicit homotopy \(s+i\lambda h(s)\) to its real projection.
Each fixed-\(\lambda\) map is a graph over \(s\), so is an
embedding on its real base. This statement retains the same
real-angle labels and original logarithmic marking.

## 3. Scope for the source

The new input is the complete positivity proof for the vertical
segment in this sector. The action identity itself is the
existing vertical-cost formula with that hypothesis now verified.
No assertion is made that a supplied arbitrary short filling has
all its real angles in (1).

The homotopy is ascending. It does not correct the previously
proved real-rim energy excess. At a nonreal critical center the
real projection has strictly larger real action; sufficiently
small inverse-period collars have their entire real rim above
the center's action, as shown in the pinned reduced-angle note.
Thus these paths do not supply lower-action side connectors.

Nor is a path to the real projection a completed dual cycle.
The original angular residue poles, fixed endpoint faces,
wire seams, full Hermite normals and free cardinal boundaries
remain to be treated in any actual source deformation.
The positivity and action calculation neither supplies their
relative homology nor estimates the full factorial density,
and gives no original-cycle coefficient or quantum lower bound.

## Direct sources and author readback

* [Original positive-edge geometry](research_positive_edge_global_monotonicity.md),
  SHA256 da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500:
  exact shape criterion, its two real-coordinate cases,
  global complete branches and face regularity, and the
  assembled accretive period Jacobian. Complete text reread.
* [Reduced-angle inverse-period graph](research_reduced_angle_inverse_period_graph.md),
  SHA256 9575d0231700e49e46ddea42c989921ce23adaafaa6e81b4f4b83c16f227f0af:
  original charged phase and inverse graph, exact vertical
  action cost, compact collar scope and real-rim excess.
  Complete text read in this sequence.

Only written proofs, source-text reads and metadata hashes were used.
No mathematical program, numerical calculation, test or compilation
was run. Adopted notes and public documents were unchanged.
