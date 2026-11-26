# Source certificates at a thin triangular boundary

This is a private continuation of the protected-sum theorem. It records
an argument to be checked independently before any extension of public
scope. The published protected operation uses two zero boundary weights.
Here the same two boundary vertices may be ordinary in the assembled
diagram. No finite polynomial factorization is asserted.

The new ingredients are a uniform boundary extension of a finite
unabridged certificate and a local comparison with a favorable boundary
correction. A proposed explicit family realizing the required boundary
ratios is given in §6. The pending audit obligations are listed in §8.

## 1. Original rates and the open block

Use the actual triangle potential
\[
 Q(w)=\max_{\alpha_i\ge0,\ \sum\alpha_i=1/2}
       \left\{\sum_i f(\alpha_i)+\sum_{w_i>0}\alpha_i\log w_i\right\},
 \qquad
 f(t)=\frac{\Lambda(\pi t)+\Lambda(\pi/2-\pi t)}{\pi}.
 \tag{1}
\]
Loads at zero weights are zero. The actual complete and one-sided rates
at quartet \((x,b,c,y)\) are
\[
 X=Q(x,b,y)+Q(x,c,y),\quad
 A_L=\max(q_c,Q(x,b,y)+q_c/2),\quad
 A_R=\max(q_b,Q(x,c,y)+q_b/2).                         \tag{2}
\]
Here \(q_i=\log w_i\); a side overloaded at a protected zero is absent.
These are the phase-uniform, full-real-spectral rates, with both
level parities and the original coefficient targets.

Let \(B\) be a fixed simple matched sphere certified at the nonmatching
mark \(uv\). Choose its marked triangle with ordinary third vertex \(b\)
and orient its quartet as
\[
             e_B=(u,a,v,b),\qquad f_B=(u,b,v).
 \tag{3}
\]
Its retained partner is \((u,a,b)\). The vertices \(a\) and \(b\)
are ordinary in this standalone marked source.

Remove \(f_B\), keeping the rooted disk \(P_B\) and all its internal
matching pairs. The interior vertices are
\(I=V(B)\setminus\{u,v,b\}\). Normalize \(b=1\). Temporarily allow
\(u,v\ge0\). Define the boundary-dependent closed expression
\[
 \widehat G_{B,\omega}(u,v;q_I)
   =\sum_{e\subset B}A_{e,\omega_e}-\sum_{i\in I}q_i-\log b.
 \tag{4}
\]
There is no target at \(u\) or \(v\) in (4). They will receive
their one original target from the surrounding core if ordinary
there. This convention is essential: making them positive in (4)
does not introduce two new coefficient demands.

Assume the old certificate is unabridged. At \(u=v=0,b=1\), every
locally allowed noncentral string has a positive interior witness
with
\[
        \widehat G_{B,\omega}\le\Phi_B-\gamma_B,
        \qquad \gamma_B>0.                            \tag{5}
\]
Witnesses may depend on the string; there are finitely many.

## 2. The complete conditional response

For every positive boundary triple, the fixed-boundary packing identity is
\[
 \inf_{q_I}\left\{\sum_{t\subset P_B}Q_t-\sum_{i\in I}q_i\right\}
                  =Q(u,v,b)+C_B.                     \tag{6}
\]
It follows from the original fixed-boundary disk theorem, not from
an exact quantum contraction. The strict Hall allocation gives
interior radii; the developed center triangles fill the prescribed
boundary center triangle with degree one. Hence the three derivatives
of the left side in the boundary logarithms are the three boundary
angles divided by \(2\pi\), exactly the derivatives of \(Q\).
Their difference is constant. The absolute constant is fixed at
one boundary triple.

The supported version with \(u=v=0,b>0\) has a finite interior minimizer,
unique after fixing \(b\). Its interior Hessian is positive definite:
the positive supported triangle Hessians are graph Laplacians, and
the ordinary graph is connected to the fixed boundary vertex \(b\).
Strict supported feasibility gives coercivity. These are the same
fixed-boundary Hall, boundary-exclusion, and development inputs used in
the earlier triangular-block response note; (6) is not being inferred
from an arbitrary stable polynomial.

Restoring \(f_B\) and its \(b\)-target gives
\[
 \inf_{q_I}\widehat P_B
   =2Q(u,v,b)-\log b+C_B.
 \tag{7}
\]
At \(u=v=0\), \(Q(0,0,b)=\frac12\log b\); thus \(C_B=\Phi_B\).
Write
\[
 T=Q(u,v,b),\qquad \Delta=2T-\log b\ge0.
 \tag{8}
\]
The conditional central minimum is exactly \(\Phi_B+\Delta\).

The minimizing interior weights converge to their positive protected
values as \(u,v\to0\), with \(b=1\). One can establish this without
differentiating a logarithm at zero. Let \(J_{u,v}\) be the disk
objective in (6). Monotonicity of \(Q\) gives \(J_{u,v}\ge J_{0,0}\).
For its protected minimizer \(q^0\),
\[
 J_{0,0}(q^{u,v})\le J_{u,v}(q^{u,v})
       \le J_{u,v}(q^0)\longrightarrow J_{0,0}(q^0).
 \tag{9}
\]
Coercivity and uniqueness of \(J_{0,0}\) therefore give
\(q^{u,v}\to q^0\). In particular the retained root middle \(a\)
is bounded below by a fixed positive number near this corner.

## 3. Uniform extension of every genuine block string

There is \(\eta_B>0\) with the following properties whenever
\[
               0\le u/b\le\eta_B,\qquad
               0\le v/b\le\eta_B.                    \tag{10}
\]
For the central string, take the conditional minimizer of §2.
For every noncentral string, including labels newly allowed when
\(u\) or \(v\) becomes positive, there is a positive interior witness
such that
\[
             \widehat G_{B,\omega}
                    \le\Phi_B-\gamma_B/2.             \tag{11}
\]
All selected witnesses, including the central conditional minimizer,
may be required to satisfy \(a\ge v\).

To prove this, first use the finite witnesses in (5) for strings
already locally allowed at the protected corner. Each retained
overloaded ordinary weight is positive and fixed. Every triangle
contains some positive ordinary coordinate, since there are only
two protected vertices. The relevant \(Q\)'s, and hence their local
rates, are continuous as \(u,v\to0\). Their finitely many inequalities
persist with half the gap.

If a string has a newly allowed side overloaded at \(u\) or \(v\),
use one fixed positive interior vector, for example \(q^0\).
Its corresponding rate is
\(\max(\log u,Q_{\text{retained}}+\frac12\log u)\), or the \(v\)
version, and tends uniformly to \(-\infty\) as \(u,v\le\eta\to0\).
All other factors are bounded above on that compact boundary square.
Thus (11) holds for these strings too, uniformly in the relative
speed at which \(u\) and \(v\) vanish. At an exactly zero overloaded
coordinate the term is simply absent.

There are only finitely many strings and selected vectors.
Their positive root weights \(a\), together with convergence in (9),
allow one further reduction of \(\eta_B\) so that \(a\ge v\).
All assertions are invariant under a common rescaling of the complete
boundary/interior vector, so the normalization \(b=1\) loses nothing.

This lemma assumes an unabridged protected certificate. Global-zero
omissions cannot be imported into the deprotected strings.

## 4. Generic bridge inequalities and the exact target correction

Let a fixed core \(D\) have its own two protected vertices, which need
not lie on the selected triangle. Its chosen crossing and triangle are
\[
              e_D=(u,v,c,b),\qquad f_D=(u,v,b).
 \tag{12}
\]
Remove \(f_D,f_B\), identify their oppositely oriented boundaries,
and pair their old partners. The new quartet is
\[
                         (u,a,c,b).
 \tag{13}
\]
No other source order changes. Put \(Q_a=Q(u,a,b)\),
\(Q_c=Q(u,c,b)\). The old central rates are \(T+Q_c\) and
\(Q_a+T\), while the new central rate is \(Q_a+Q_c\).

If \(a\ge v\) and \(c\ge v\), monotonicity gives
\(Q_a,Q_c\ge T\). The three exact comparisons are
\[
 \begin{array}{c|c|c}
 \text{new label}&(\text{core},\text{block})&\text{local bound}\\ \hline
 C&(C,C)&X_{\text{new}}=X_D+X_B-2T\\
 L&(L,C)&A_{{\text{new}},L}\le A_{D,L}+X_B-2T\\
 R&(C,R)&A_{{\text{new}},R}\le X_D+A_{B,R}-2T .
 \end{array}                                           \tag{14}
\]
For the left case the right side is
\(\max(q_c+Q_a-T,Q_a+q_c/2)\), which bounds the new rate
when \(Q_a\ge T\). The right case is identical using \(Q_c\ge T\).
The middles \(a,c\) are taken ordinary in the application below.

The only duplicated target is that at \(b\): the core already
contains its \(u,v\) targets when they are ordinary, and (4) contains
none at those vertices. Each fresh block interior vertex receives
one target. Thus the full shared functions obey
\[
 G_{{\text{new}},\omega}
       \le G_{D,\omega_D}+\widehat G_{B,\omega_B}-\Delta.
 \tag{15}
\]
In the central case this is equality. No boundary corner is
independently reweighted, and no target is split fractionally.
For every noncentral output at least one induced input is noncentral.

The classical disk identity also gives, before any source estimate,
\[
                      \Phi_{\text{new}}=\Phi_D+\Phi_B.
 \tag{16}
\]
At fixed core weights the block contributes exactly the removed
triangle potential plus \(\Phi_B\); all core face derivatives and
ordinary demands are therefore retained.

## 5. A finite, usable core hypothesis

Suppose the core has an unabridged finite shared-radius certificate.
Choose one witness for every noncentral induced core string and
the complete vector for its central string. Require at the selected
triangle that every selected vector satisfy (10) and \(c\ge v\).
This is a finite condition on pre-existing witnesses, not an assumed
gap for the assembled diagram.

Use the matching block witness from §3 at each chosen core boundary
triple. If the block string is central, its exact value
\(\Phi_B+\Delta\) cancels the correction in (15).
If noncentral, (11) and \(\Delta\ge0\) supply a loss of at least
\(\gamma_B/2\). Consequently
\[
 G_{{\text{new}},\omega}\le
 \Phi_D+\Phi_B-\min(\gamma_D,\gamma_B/2)
                       \quad(\omega\ne C).             \tag{17}
\]

The same argument handles any fixed finite collection of such
attachments at distinct core matching regions. No selected face or
its partner is part of another selected pair. Their boundary
vertices may coincide: their weights are the same core weights.
Fresh block interiors are disjoint. The corrections in (15) add,
with one subtraction for each duplicated \(b\)-target. Choose a
single induced core witness, then each block witness at its actual
boundary weights. The gap is at least the minimum of the core gap
and the finitely many half block gaps.

The literal sphere gluing retains a simple triangulated sphere and
perfect matching. The core protected edge is untouched. The general
Morse inverse cut supplies its original augmented link in \(S^3\)
and its disk-framed primitive curves. Choose a terminal parity
pattern passing the assembled one-component test.

The proof of the volume consequence would then be exactly the
published Appendix N/O transfer: the phase-uniform sector estimates
give the full complementary polynomial a gap on its entire real
spectral cube at both parities; the finite Hermite norm inserts all
fixed powers without exponential cost; the nonzero entire central
period tends to (16) for independent long signed primitive fillings.
The positive original cells, primitive equations, main cusp, and
same-chain calibration identify its rate with the actual filled
knot-complement volume. No filling threshold uniform over growing
cores or blocks is asserted.

## 6. Explicit thin faces in strictly balanced cores

There is a proposed exact family satisfying the finite core condition
with one complete vector for every string. Start with the octahedral
white sphere: poles \(P,S\), rim \(v_0,v_1,v_2,v_3\), with protected
mark \(v_0v_1\). Write
\[
 T_j=(P,v_{j+1},v_j),\qquad
 Z_j=(S,v_j,v_{j+1})\quad(j\bmod4).
 \tag{18}
\]
Match \(T_0\) with \(T_1\), \(Z_0\) with \(Z_1\), \(T_2\) with
\(Z_2\), and \(T_3\) with \(Z_3\). Its marked complete curvatures are
\[
        P=S=1,\quad v_2=v_3=2,\quad v_0=v_1=0.
 \tag{19}
\]
The original face-star equations verify (19). For instance the pole
has one singleton half-load, two loads
\(\pi^{-1}\arctan(1/\sqrt2)\), and one load
\(\pi^{-1}\arctan(1/(2\sqrt2))\), summing to one. The rim equations
follow by the complementary two-angle identities.

Put \(u=v_2\), \(v=P\), \(b_0=v_3\), \(c=S\). The triangle
\(F_0=(u,v,b_0)=T_2\) is paired with \((u,b_0,c)=Z_2\).
Insert \(b_j\) into \(F_{j-1}\), replacing it by
\[
 F_j=(u,v,b_j),\quad
 A_j=(u,b_j,b_{j-1}),\quad
 B_j=(v,b_{j-1},b_j).
 \tag{20}
\]
This is the ordinary oriented stellar insertion in the actual
interstice. The unique fixed-boundary packing has
\[
 b_j=3j^2+4\sqrt2\,j+2
       =3(j+\sqrt2)(j+\sqrt2/3).                       \tag{21}
\]
Indeed the positive Descartes recurrence is
\(b_{j+1}=b_j+3+2\sqrt{3b_j+2}\), and
\(\sqrt{3b_j+2}=3j+2\sqrt2\). Every new disk lies inside its
predecessor's triangular interstice. The old exterior disks do not move.

Take any positive even number \(n\). Change the matching in this disk
as follows: pair \(A_1\) with the old exterior \(Z_2\), pair
\(F_n\) with \(A_n\), and for \(1\le j<n\) pair \(B_j,B_{j+1}\)
when \(j\) is odd and \(A_j,A_{j+1}\) when \(j\) is even.
This exhausts every new triangle once. The matching sides are
respectively \(ub_0\), \(ub_n\), and \(s_jb_j\), where \(s_j=v\)
for odd \(j\) and \(s_j=u\) for even \(j\). They are actual boundary
edges with opposite orientations in (20), not artificial tangle edges.

All matching regions are strictly balanced. Here are explicit
uniform lower bounds for their larger middle comparison.
Let \(g=f(1/4)\), \(b_1=5+4\sqrt2\), \(b_2=14+8\sqrt2\).
The two unchanged protected caps have
\[
       X-\log2\ge 2g-\tfrac34\log2>0.06.
 \tag{22}
\]
The remaining unchanged matching region has positive outer
curvature and middle weights one, so its strict comparison is immediate.

For the root region with outer weights \(2,2\), middle weights
\(b_1,1\), allocate triangle loads
\((1/12,1/3,1/12)\) and \((1/5,1/10,1/5)\). This gives
\[
 X-\log b_1\ge
 2f(1/12)+f(1/3)+2f(1/5)+f(1/10)
       +\tfrac{17}{30}\log2-\tfrac23\log b_1>0.25.
 \tag{23}
\]
For an internal matched pair, use loads \(1/4,1/4\) at
\(b_j,b_{j-1}\) in one triangle and at \(b_j,b_{j+1}\)
in the other; assign zero load at \(s_j\). Then
\[
 X-\log b_{j+1}\ge
 4g-\tfrac14\log\frac{b_{j+1}^{\,3}}{b_j^2b_{j-1}}
 \ge4g-\tfrac14\log\frac{b_2^3}{2b_1^2}>0.09.
 \tag{24}
\]
The middle inequality follows because the ratios \(b_j/b_{j-1}\)
decrease, by the factorization in (21). The expression inside the
first logarithm is \((b_{j+1}/b_j)^3(b_j/b_{j-1})\).

At the final pair, the outer weights are \(2,b_n\), and the
middles are \(1,b_{n-1}\). A vertex allocation at \(b_n\) and a
quarter-quarter allocation at \(b_n,b_{n-1}\) give
\[
              X-\log b_{n-1}
                  \ge2g+\tfrac34\log(b_n/b_{n-1})>0.
 \tag{25}
\]
This also bounds the smaller middle comparison. Every surviving
overloaded triangle has two positive corners, hence its mixed-branch
loss \(Q_z-\frac12\log z\) is strictly positive. For each fixed
finite \(n\), the complete vector therefore gives an unabridged
strict sector certificate directly; no uniform-in-\(n\) lower bound
for this latter loss is needed.

The terminal face \(F_n\) has three ordinary vertices. Its exact
boundary ratios and opposite middle satisfy
\[
        u/b_n=2/b_n\longrightarrow0,\qquad
        v/b_n=1/b_n\longrightarrow0,\qquad
        c_{\text{tip}}=b_{n-1}\ge v.
 \tag{26}
\]
Thus every fixed certified protected block can meet the condition
of §5 on this family by taking a sufficiently large even \(n\).
The mark remains the original \(v_0v_1\); it is not moved to the
new separating triangle.

The three numerical thresholds in (22)–(24) are only fixed elementary
constant inequalities. The accompanying interval script proves them
from the Lobachevsky Fourier series with its explicit tail. The
proof for every even \(n\) is the exact ratio argument above, not
a test over finitely many chain lengths.

## 7. Many distinct interfaces and the separation from weak balance

A finite number of octahedral cores may first be joined at their
protected marked triangles using the published protected-sum theorem.
Keep their \(T_2,Z_2\) pairs untouched. Their complete curvatures
are retained after the joining scale is fixed, and the resulting
core remains strictly balanced. Build one even chain in each selected
\(T_2\) disk and perform the local matching change in §6. The root
pairs are distinct; the old protected gluing comparisons elsewhere
are unchanged. The inequalities (22)–(25) prove strict balance
for the resulting finite core.

For any fixed finite list of unabridged certified blocks, choose
the even chain lengths large enough for their individual \(\eta_B\)
and attach them at the distinct terminal faces. Boundary vertices
may be shared; their curvatures and targets are still single core
coordinates. This is the finite multi-interface application of §5.

For the seventeen-region seed, choose its crossing-15 marked
triangle. Its four possible weak-balance failures at \(2,4,7,12\)
are untouched. The restricted rational dual certificate gives
\[
 \max_{e\in\{2,4,7,12\}}\max_{z\ \text{ordinary middle}}
              (\log z-X_e)>1/160
 \tag{27}
\]
at its protected complete packing: the four nonnegative defects
bound above the restricted dual excess, which is greater than
\(0.025\). Its ordinary overloaded middle is retained. Conditional
interior continuity from (9) therefore keeps a strict failed
comparison for sufficiently small positive boundary ratios.

Consequently these proposed assemblies need not satisfy complete
weak balance at their original core mark, even though the finite
source argument uses that mark throughout. Several separating
triangles use different edges; the construction is not merely
iteration at one protected pair. This is a marked-source statement.
No assertion is made that the resulting knots lack another known
presentation or another usable mark. Diagrams and knot types can
change in this construction.

## 8. Freeze status and remaining obligations

The exact bridge comparison (14), target identity (15), suppression
of newly deprotected labels, and the finite witness selection are
the proposed analytic mechanism. No bound for generic stable binary
polynomials, no far-node spectral gap, and no exact quantum
star-triangle factorization is used.

Before promoting this to an established new volume class, an
independent reader should check:

* the fixed-boundary identity and supported coercivity used in (6)–(9)
  against the literal simple-sphere disk theorem;
* the oriented octahedral/chain matching in (18)–(20), its primitive
  inverse-cut framing, and the finite multi-interface target counts;
* the extension over all newly allowed labels in §3 and the local
  comparisons in every sector of (14);
* the unchanged hypotheses of the full-source-to-Hermite and
  central-period-to-metric-volume theorems for the assembled diagram.

The new source range has not been added to public statements.
The fixed constant verifier does not replace those geometric or
asymptotic proofs. No assertion about a growing diagram as the
quantum level grows is intended.
