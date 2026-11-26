# A regular midpoint frame for complete knot holonomy

Private written proof, 18 November 2026.

The actual braid coordinates admit a regular geometric frame with
cut position exactly \(A_{\rm cut}=-1\). This holds for every
complete hyperbolic knot holonomy and every fixed finite braid
word, using the five-shape crossing chart of M below. It
strengthens the generic-frame statement by fixing the midpoint
position in advance.

The obstruction to this choice would be a group element acting
as half of the primitive meridian translation. The complete cusp
lattice excludes it. The remaining frame parameter can then be
chosen from a finite predetermined rational grid.

This is a statement about the actual classical braid chart.
It neither identifies the integration cycle of the binomial cut
nor proves that a geometric contribution survives in the invariant.

## 1. Cusp normalization and the midpoint meridian

Let \(\rho_0\) be the complete faithful projective holonomy of
a hyperbolic knot complement. Choose its oriented peripheral
basis \((\mu,\lambda)\). Normalize the cusp fixed point to
\(\infty\), and the meridian translation to one. Then
\[
 \rho_0(\mu)=J_1,\qquad
 \rho_0(\lambda)=J_\tau,\qquad
 J_z=\begin{pmatrix}1&z\\0&1\end{pmatrix},\qquad
 \Im\tau>0.
 \tag{1}
\]
Here the full stabilizer of this cusp point is
\[
 \operatorname{Stab}_{\rho_0(\pi_1)}(\infty)
       =\{J_{m+n\tau}:m,n\in\mathbb Z\}
 \quad\hbox{in }\mathrm{PSL}_2(\mathbb C).
 \tag{2}
\]
Equation (2) uses the full peripheral group of an embedded
complete torus cusp, not a proper sublattice. Indeed a lift of
that cusp is a horoball whose deck stabilizer is the fundamental
group of its torus quotient. Taking the horoball far enough out
identifies this stabilizer with the full parabolic fixed-point
stabilizer. The meridian is primitive in that torus lattice.
Consequently \(J_{1/2}\) is not the image of any group word:
\(m+n\tau=1/2\) forces \(n=0\) and then an impossible integer
\(m=1/2\).

For \(s\ne0\), use the change of projective frame
\[
 F(r,s)=\begin{pmatrix}r&1-r\\s&-s\end{pmatrix},\qquad
 F(r,s)^{-1}=
 \begin{pmatrix}1&(1-r)/s\\1&-r/s\end{pmatrix}.
 \tag{3}
\]
It sends the selected flag \((1,1)\) to \(\infty\), and
\[
 F(r,s)^{-1}J_1F(r,s)
       =\begin{pmatrix}1+s&-s\\s&1-s\end{pmatrix}.
 \tag{4}
\]
At \(s=-2\), the actual convention of M is \(G=-\mu\),
\(x=-1\), so the cut coordinates are
\[
 \mu_{\rm cut}=\begin{pmatrix}-1&2\\-2&3\end{pmatrix},
 \quad K=1,\quad e=-2,\quad f=2,\quad
 A_{\rm cut}=x/K=-1,\quad p_{\rm new}=1.
 \tag{5}
\]
The last equality follows directly from M's physical relation
\(f=(1-A)/p_{\rm new}\). Thus (5) is the actual midpoint
position and selected flag, with a noncentral complete meridian.

## 2. A prefix minor cannot vanish throughout this slice

Let \(P\) be any determinant-one matrix representing the
projective image of a group word, and write
\[
 P=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]
The letter \(d\) in this section is a matrix entry, not a quantum
dimension. Multiplication of (3) gives
\[
 (F^{-1}PF)_{11}
 =\frac cs r(1-r)+(a-d)r+d+bs .
 \tag{6}
\]
For fixed nonzero \(s\), this polynomial is identically zero
in \(r\) precisely when
\[
 c=0,\qquad a=d,\qquad d+bs=0.
\]
The determinant then gives \(d^2=1\), so this case is exactly
\[
 P=\pm J_{-1/s}.
 \tag{7}
\]
At \(s=-2\), (7) contradicts (2). Therefore every such prefix
minor has at most two exceptional values of \(r\).
Signs of determinant-one lifts do not affect this argument:
both the zero condition and (2) are projective statements.

This is the reason for the midpoint choice. A general fixed
slice \(s\) can fail this test if \(-1/s\) is an actual
peripheral translation.

## 3. The other finite braid-chart conditions

Keep any fixed finite braid presentation and the actual
holonomy-braiding convention of M. At each stage its strand
meridians are conjugates of the knot meridian. Every ordered
prefix \(P_j=H_j\cdots H_1\), with \(H_j=-\mu_j\), is up to
its central sign the image of a group word. The same is true
at intermediate braid stages by the explicit Wirtinger rule.
Thus Section 2 applies simultaneously to all prefix minors.

For clarity the remaining nonvanishing conditions can also
be checked on this fixed slice. Put
\[
 v_r=\begin{pmatrix}r\\s\end{pmatrix},\qquad
 \alpha_r=(1,(1-r)/s),\qquad \alpha_r(v_r)=1.
 \tag{8}
\]
They are the first column of \(F\) and first row of \(F^{-1}\).
Each varies injectively in its affine projective-line chart.
Once the prefix minors are nonzero, the Gauss inverse of M
has
\[
 e_j=0\ \Longleftrightarrow\
       \alpha_r\hbox{ is a left eigenline of }H_j,
 \tag{9}
\]
\[
 f_j=0\ \Longleftrightarrow\
       v_r\hbox{ is an eigenline of }
                         P_{j-1}^{-1}P_j .
 \tag{10}
\]
Here the matrices on the right are in the unframed
normalization of (1); their framed representatives are used
on the left.

One can verify these tests directly. If
\(P_{j-1}=(p_{uv})\), the lower Gauss factor is
\[
 B_-(P_{j-1})=\begin{pmatrix}1&0\\-p_{21}&p_{11}\end{pmatrix}.
\]
The upper-right entry of
\(B_-(P_{j-1})H_jB_-(P_{j-1})^{-1}\) is
\((H_j)_{12}/p_{11}\). Its vanishing says that the first
dual basis row is a left eigenline, proving (9) after
undoing \(F\). The lower-left entry vanishes precisely
when \(P_{j-1}e_1\) is an eigenvector of \(H_j\), or
equivalently when \(e_1\) is an eigenvector of
\(P_{j-1}^{-1}H_jP_{j-1}=P_{j-1}^{-1}P_j\).
This proves (10).

Each matrix in (9)--(10) is a noncentral parabolic:
the second is a conjugate of the corresponding meridian.
It has a unique projective eigenline. Consequently each
condition excludes at most one value of \(r\).

There are only finitely many stages and strands. Choose
one \(r\) outside all their exceptional values. Then all
\(K_j,e_j,f_j\) are nonzero, and the actual positive and
negative crossing denominators are nonzero. In the complete
case \(x^2=1\), the physical identity
\[
 e_jf_j=\frac{(1-A_j)(1-x^2/A_j)}x
\]
also excludes \(A_j=1\), both before and after every crossing.
The transfer shape \(C\ne1\) follows from the nonzero product
\(e_1f_2\), or its negative-crossing counterpart. M's five
ordered crossing shapes consequently avoid both zero and one.
This proves regularity in that five-shape chart; it is not a
claim that a four-term subdivision has no pinched crossing.

## 4. A finite rational choice and bounded frame

Let \(p\) count the prefix minors tested above, and let
\(q_+\), \(q_-\) count the eigenline tests (9), (10).
There are at most
\[
                         B=2p+q_++q_-
\]
bad complex numbers \(r\). One of the \(B+1\) predetermined
rational values
\[
 r_k=\frac{k}{B+2},\qquad 1\le k\le B+1
 \tag{11}
\]
therefore works. In particular it can be chosen in \((0,1)\).
At \(s=-2\), the ordinary Euclidean matrix norms satisfy
\[
                    \|F(r,-2)\|\le3,\qquad
                    \|F(r,-2)^{-1}\|\le3/2 .
 \tag{12}
\]
These follow by bounding their Frobenius norms in (3).
The normalization of the complete cusp in (1) has already
been made; (12) does not bound the original cusp-normalizing
conjugation or the entries of every other holonomy.

If the unframed matrices lie in a coefficient field \(k\),
this choice of frame uses only rational coefficients and
preserves that field. No degree bound for \(k\) is asserted.
The finite count does not give a uniform lower bound on all
chart denominators over a degenerating family of knot
holonomies. For each fixed complete representation they
are finitely many nonzero numbers, which is sufficient for
an open neighborhood.

## 5. A selected-flag deformation through the same midpoint

There is an explicit local extension beyond the complete
meridian. Work on any augmented holomorphic representation
family near \(\rho_0\), with chosen meridian eigenvalue
\(M^{-1}\) and eigenflag. A local frame sends that flag
to \(\infty\), putting the meridian in upper triangular form.
Its off-diagonal entry is a unit at completion, so a diagonal
change normalizes it to one. Thus it has the form
\[
 J_M=\begin{pmatrix}M^{-1}&1\\0&M\end{pmatrix}.
\]
Keep a good rational \(r\) from (11), and define
\[
 s(M,r)=-2M-(M^{-1}-M)r,\qquad F_M=F(r,s(M,r)).
 \tag{13}
\]
The function \(s\) is nonzero near \(M=1\).
Direct multiplication gives
\[
 F_M^{-1}J_MF_M
 =\begin{pmatrix}-M&M+M^{-1}\\-2M&2M+M^{-1}\end{pmatrix}.
 \tag{14}
\]
It is independent of \(r\), its selected eigenvector is
\((1,1)\), and the actual cut symbols with \(x=-M\) are
\[
 K=M,\qquad e=-(M+M^{-1}),\qquad f=2,\qquad
 A_{\rm cut}=-1,\qquad p_{\rm new}=1.
 \tag{15}
\]
These agree with the literal symbol formulas of M.
Every other prefix minor and crossing denominator that was
nonzero at \(\rho_0\) remains nonzero on a sufficiently small
neighborhood of the augmented family. The matrices \(F_M\)
and their inverses remain bounded there.

The existence and parametrization of that augmented family
are not proved by this change of frame. The assertion is
that whenever the marked family is supplied, (13) puts it
in this same actual midpoint chart. No square-root choice
or change of the selected peripheral eigenflag is hidden.

## 6. Consequences and the remaining quantum question

The complete geometric representation has a regular point
in the actual source's classical chart with \(A_{\rm cut}=-1\),
and this choice persists on a marked nearby deformation.
Thus midpoint framing is not excluded by a generic chart
divisor, for any fixed finite braid of a hyperbolic knot.
No alternating or long-twist hypothesis is used.

The parameter \(r\) has not been integrated out. At fixed
cut meridian, varying it is the residual peripheral
centralizer action. A binomial cut also changes the
boundary phase and its stationary equations. Its
concentration near the middle occupation does not, by
itself, identify its critical scheme or its original
relative integration cycle with this classical slice.
The normal residue and the off-divisor source remain
different data.

In particular this lemma gives no nonzero geometric cycle
coefficient or scalar lower bound, and proves no new
volume-conjecture filling case. It supplies the regular
classical target for the source comparison.

## Coverage and complete proof-source pins

Existence of diagrammatic solutions associated with
representations has substantial prior coverage, including
[Cho--Yoon--Zickert, *On the Hikami--Inoue conjecture*](https://arxiv.org/abs/1805.11841).
Their stated cluster-coordinate criterion retains a
boundary-parabolic lift obstruction. The present calculation
uses projective group words in the actual five-shape
crossing chart and does not identify that chart with their
cluster variables or discard their lift condition.
The recent
[arc-faithful braid statement](https://arxiv.org/abs/2611.13305)
concerns nondegenerate four-term octahedral shapes after
rewording. Neither paper's proof is used here. No novelty
claim is made for general representation-associated
critical-point existence.

* M: notes/marked_braid_holonomy.md, SHA256
  eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.
* I: notes/research_fixed_interior_cut_source.md, SHA256
  93b2887527e0b5c9cb93f4da77702c996f0524e0a93f0c0032909345efdbd1b2.

M supplies the actual rational crossing/holonomy map,
Gauss inverse, selected-flag convention and five-shape
chart. I fixes the interpretation of midpoint cut position.
All matrix calculations, the fixed-slice exclusion,
finite-grid choice and local deformation are proved above.
The complete unchanged M and I were read in the author
sequence, their used implications checked and matching
hashes renewed. Only written mathematics and text/hash
operations were used. Frozen and public files are unchanged.
