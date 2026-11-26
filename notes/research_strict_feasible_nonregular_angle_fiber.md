# A strictly feasible nonregular angle fiber with a positive filling center

Private written proof, 17 November 2026.

The regular fiber locus in the reduced-angle graph theorem can be a
proper subset of its strictly feasible real-angle domain, even for an
original tree that has a positive charged filling center. The point is
to keep the real angles fixed: at zero real angles, the fiber does not
depend on the signed powers. Thus the existing zero-power corner
minimum persists as a fiber minimum after the powers become large.
The full minimum then moves to an interior point near completeness.

This is a limitation of a proposed global geometric graph extension.
It is not a statement about cancellation in the original finite
source, a knot invariant, or hyperbolicity of a filled manifold.

## 1. The original tree and its fixed fiber

Take two adjacent selected vertices \(v,w\), each of degree three.
Attach two distinct outside leaves to each selected vertex, and fix
all four outside angles at zero. There are six vertices and five
edges. Set \(c_v=c_w=1\), and retain arbitrary real signed powers
\(n_v,n_w\). The original convention remains \(n_a=\eta_a-2p_a\)
when these data come from integral fillings.

Write \(t_a=s_a+i h_a\) and \(g_{a,e}=\Im r_{a,e}\). The affine
rows, positivity inequalities and square coordinates are
\[
\begin{gathered}
 \sum_{e\ni a}g_{a,e}-\frac{n_a}{2}s_a=-\pi
                         \qquad(a=v,w),\\
 |s_a|+2|g_{b,e}|<\pi,\qquad
 |s_b|+2|g_{a,e}|<\pi\qquad(e=ab),\\
 A_P=s_a/4-g_{b,e}/2,\quad A_Q=s_a/4+g_{b,e}/2,\\
 y_P=g_{a,e}/2+s_b/4,\quad y_Q=g_{a,e}/2-s_b/4.
\end{gathered}                                                    \tag{1}
\]
All outside \(s_b\) are zero. The energy is the original
\[
             \mathcal E=4\sum_e\{E(A_{P,e},y_{P,e})
                                     +E(A_{Q,e},y_{Q,e})\}.        \tag{2}
\]
It is independent of the powers; their only occurrence is in the
affine rows in (1).

Let \(D_n\) be the projection of the strict feasible set to
\((s_v,s_w)\). Let \(D_{\mathrm{reg},n}\) consist of those points
of \(D_n\) whose closed fiber minimum is interior, exactly as in
the reduced-angle graph theorem.

**Proposition 1.** For every real pair \((n_v,n_w)\),
\[
                      (0,0)\in D_n\setminus D_{\mathrm{reg},n}.
                                                                    \tag{3}
\]
Its closed fiber has the same unique minimizer for every pair:
\[
\begin{array}{c|c}
\text{incidence}&g\\ \hline
\text{either endpoint of the internal edge }vw&-\pi/2\\
\text{selected endpoint of each of the four outside edges}&-\pi/4\\
\text{outside endpoint of each outside edge}&0 .
\end{array}                                                        \tag{4}
\]

**Proof.** At \(s_v=s_w=0\), the rows become
\[
                   \sum_{e\ni v}g_{v,e}
                   =\sum_{e\ni w}g_{w,e}=-\pi.                    \tag{5}
\]
Neither these rows, the bounds \(|g_{a,e}|\le\pi/2\), nor (2)
depends on \(n_v,n_w\). A strictly feasible point of this fiber
puts \(-\pi/3\) at every selected incidence and zero at every outside
incidence. Thus \((0,0)\) is an interior point of the projected
strict domain \(D_n\), for every pair.

Section 6 of the pinned convex-variation source proves that (4),
with \(s_v=s_w=0\), is the minimum of the full zero-power,
unit-charge problem. Section 5, Corollary 3 there proves its
uniqueness, including against boundary assignments. It is therefore
also the unique minimum of its fixed-\(s\) fiber. The equality of
fibers and energies just proved transfers this exact minimum to
every power pair.

For clarity, the limiting argument in that source does not assume
an interior minimum at unit charge. For charges
\(c_v=c_w=\lambda\in(0,1)\), the symmetric purely imaginary solution
\(t_v=t_w=-ih_\lambda\) is determined by
\[
 2\arcsin(\tanh(h_\lambda/2))
       +\arcsin(\sinh(h_\lambda/2))=\pi\lambda,\qquad
                 0<h_\lambda<2\operatorname{arsinh}1.             \tag{6}
\]
The left side increases from zero to \(\pi\). These interior
minima converge to (4). Scaling any feasible unit-charge angle
assignment by \(\lambda\) gives a feasible charge-\(\lambda\)
assignment. Continuity of the original square energy then proves
the minimum comparison at the limit.

At (4), the internal edge has square coordinates
\[
       (A_P,y_P)=(\pi/4,-\pi/4),\qquad
       (A_Q,y_Q)=(-\pi/4,-\pi/4).                                 \tag{7}
\]
Both factors are corners; its original edge root is \(q_{vw}=0\).
Every outside square is interior, with \(A_P=A_Q=0\) and
\(y_P=y_Q=-\pi/8\) when oriented from the selected endpoint.
Thus the fiber minimum is not interior, proving (3). \(\square\)

## 2. A positive full center for large powers on the same tree

**Proposition 2.** There is \(\nu_0>0\) such that for equal signed
powers \(n_v=n_w=\nu>\nu_0\), the original unit-charge equations
have a positive solution on the complete branches. It is the
unique full minimum, and
\[
 t_v=t_w=\frac{2\pi}{\nu}
                 -\frac{6\pi i}{\nu^2}+O(\nu^{-3}).                \tag{8}
\]
Consequently \(D_{\mathrm{reg},n}\) is nonempty and properly
contained in \(D_n\) for every such \(\nu\).

**Proof.** The local analyticity needed here follows directly from
the original square dictionary. For one edge write
\(f(P)=\arctan(\tanh P)\), so \(f(P)=P+O(P^3)\) near zero.
Combining the real identities of the convex-variation source gives
the holomorphic identities
\[
\begin{aligned}
t_a&=2\{f(P)+f(Q)\},&t_b&=-2i(P-Q),\\
r_{a,e}&=P+Q,&r_{b,e}&=-i\{f(P)-f(Q)\}.
\end{aligned}                                                     \tag{9}
\]
The derivative of the map \((P,Q)\mapsto(t_a,t_b)\) at zero is
invertible. Its local inverse is odd and analytic. Thus the original
returns are analytic near complete angles and
\[
 r_{a,e}=\frac{t_a}{2}
                 +O((|t_a|+|t_b|)^3),\qquad
 r_{b,e}=\frac{t_b}{2}
                 +O((|t_a|+|t_b|)^3).                             \tag{10}
\]
For small complex angles the reconstructed strip variables remain
in \(|\Im P|,|\Im Q|<\pi/4\); all original edge factors are
positive, with their branches continued from completeness.

Put \(R_a(t)=\sum_{e\ni a}r_{a,e}(t)\), keeping the four outside
angles exactly zero. The selected degrees are three, hence
\[
 R(0)=0,\qquad
 R_a(t)=\frac32 t_a+O(\|t\|^3)\qquad(a=v,w).                        \tag{11}
\]
Writing \(\epsilon=\nu^{-1}\), the unchanged filling equations
\(R_a-i\nu t_a/2=-\pi i\) are equivalent, for \(\epsilon\ne0\), to
\[
        \mathcal F(t,\epsilon)
          :=t+2i\epsilon R(t)-2\pi\epsilon(1,1)=0.                 \tag{12}
\]
At \((t,\epsilon)=(0,0)\), the derivative \(\mathcal F_t\) is
the identity. The holomorphic implicit-function theorem therefore
gives a unique small solution \(t(\epsilon)\). Equation (12) first
gives \(t=2\pi\epsilon(1,1)+O(\epsilon^2)\); substitution of (11)
gives
\[
                 t=2\pi\epsilon(1,1)
                        -6\pi i\epsilon^2(1,1)+O(\epsilon^3).
                                                                    \tag{13}
\]
Interchanging \(v,w\) and their pairs of leaves preserves (12);
local uniqueness makes the two components equal. For positive
small \(\epsilon\), (9) proves positivity and (13) puts both
selected angles in the lower half-plane.

The original variational theorem now identifies this solution
with the unique interior global minimum of (2) on its own charged
polytope. Its real-angle projection belongs to
\(D_{\mathrm{reg},n}\). Proposition 1 supplies the strictly feasible
point \((0,0)\) outside that locus. \(\square\)

The conclusion holds in particular for all sufficiently large
integer \(\nu\). If a common original half-twist parity is fixed,
one may restrict \(\nu\) to that parity, so that
\(p_a=(\eta_a-\nu)/2\) is an integer. The proof does not change a
carrier or replace a primitive filling slope.

## 3. Consequence and limit of the example

The example excludes the implication
\[
 \text{strict fiber feasibility plus a positive full center}
            \quad\Longrightarrow\quad D_{\mathrm{reg},n}=D_n.    \tag{14}
\]
It uses a tree, complete outside angles, unit charges, and the
original square energy throughout. A leaf-removal or flow argument
cannot establish (14) under just those hypotheses.

The reduced-angle theorem's compact low-energy collars remain
valid around the center (8). Their energy condition excludes the
corner fiber in (4); strict linear feasibility alone does not.
No assertion is made here about the topology of the regular locus,
an alternative positive cell decomposition, or a contour avoiding
this particular boundary fiber. There is no finite-source bound,
signed-period lower estimate, or knot-conjecture counterexample.

## Direct sources and author procedure

* [Original convex variation](research_positive_filling_convex_variation.md),
  SHA256
  2777b2bcb149d64a79757ba64ccb16be5438cf37ce820ad50c5f532afd8fc6c0.
  The complete text was read in this author sequence. Sections 1--2
  give the square dictionary used in (9); Sections 3--5 give the
  energy, original equations and uniqueness; Section 6 supplies
  the original zero-power corner minimum and its limiting proof.
* [Reduced-angle inverse-period graph](research_reduced_angle_inverse_period_graph.md),
  SHA256
  9575d0231700e49e46ddea42c989921ce23adaafaa6e81b4f4b83c16f227f0af.
  The complete text was read in this author sequence. Sections 1--2
  define \(D_n\), its regular fiber locus and the exact positive
  period graph; Section 3 gives the retained low-energy collars.

This note uses written derivations, source-text reads and metadata
hashes only. No mathematical program, numerical computation, test,
build or compilation was run. Frozen notes and public files were
unchanged.
