# A source-preserving presentation with one initialized Euler star

Private written proof, 19 November 2026.

Every irreducible complete geometric braid tuple admits a
source-preserving presentation whose total product is regular
semisimple and whose actual reduced word has exactly one Euler
star. That star is positive and its donor is the resolved lower
row. At most three positive left Markov stabilizations are needed,
with actual braid conjugations between them.

This reduces the geometric donor-initialization problem to one
boundary star. It does not estimate the other physical crossing
kernels, the gauge interfaces, or the original closed period.
The complete proof directs are R and G, pinned below.

## 1. The literal left stabilization and its source scalar

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\).
The common meridian varies at this fixed quantum root. Put
\[
 x=-M/q,\qquad g=K^{1-N},\qquad
 \alpha(M)=\kappa(M)x^{1-N}.
 \tag{1}
\]
All factors have the balanced basis of R. For an actual
analytic braid intertwiner \(W(M)\) on \(m\) heads, retain
the original pointed source
\[
 \Phi_m(W)=\operatorname{Tr}
       \bigl((P_0\otimes g^{\otimes(m-1)})W\bigr).
 \tag{2}
\]
Every common crossing scalar is included in \(W\). A separately
specified dimension or framing line remains separately specified.

Let \(\iota\) shift every braid-generator index by one and set
\[
                  W^{\rm L}=R_1(I\otimes W).
 \tag{3}
\]
This is a positive left Markov stabilization. The first input
occupation of \(R_1\) is zero in the source (2), so its literal
finite row is
\[
 R_1(w_0\otimes w_b)
                  =\kappa x^{-b}w_b\otimes w_0 .
 \tag{4}
\]
There is no transfer term in (4): the donor lowering operator
annihilates \(w_0\). In the trace defining
\(\Phi_{m+1}(W^{\rm L})\), the new first output occupation must
also be zero. Thus (4) forces \(b=0\). Its second output is
then zero, so the second traced input is zero as well.
The pivot on that head contributes \(g_0=x^{1-N}\).
All remaining entries are precisely the old pointed trace.
Consequently, as an identity of actual meridian families,
\[
             \boxed{\ \Phi_{m+1}(W^{\rm L})
                              =\alpha(M)\Phi_m(W).\ }
 \tag{5}
\]
The proof has used only finite entries and physical endpoints.
It has not replaced a pivotal partial trace by a generic
quantum-dimension formula.

The prescribed zero-framing compensation is
\(\alpha^{-\operatorname{wr}}\). The writhe increases by one,
so (5) proves exact preservation of the normalized source,
including its fixed-\(q\) meridian germ and every derivative.
R proves the same source cyclicity for actual total
intertwiners. Hence actual braid conjugations may be inserted
between these left stabilizations without changing that
normalized source. The assertion is not made for arbitrary
marked matrices that fail the total intertwining equations.

## 2. The last stabilization leaves exactly one Euler star

Write \(W_*\) for the entire braid word just before the last
left stabilization, including all earlier conjugations and
stabilizations. If it acts on \(r\) heads, the final word
acts on \(r+1\) heads and has the literal form
\[
                 W_{\rm fin}=R_1(I\otimes W_*).
 \tag{6}
\]
Every generator of \(I\otimes W_*\) has index at least two.
Thus (6) contains exactly one generator of index one,
and that generator is positive. No cancellation or
semiclassical rewriting is needed for this statement.

R's actual constant-prefix algebra map gives
\[
 \boxed{\quad
 \mathcal B_{r+1}(W_{\rm fin})
       =\kappa S_rD_{\rm red}\,W_* .
 \quad}
 \tag{7}
\]
On the right \(W_*\) is the original physical braid matrix
on the remaining \(r\) heads, with its original generator
indices. The rightmost factor acts first. Explicitly,
\[
 \begin{split}
 S_r&=\sum_{n=0}^{d}
              \frac{(x^{-1}L_1F_{\rm tail})^n}{(Q;Q)_n},\\
 D_{\rm red}w_a&=(-1)^aQ^{a(a-1)/2}x^{-2a}w_a .
 \end{split}
 \tag{8}
\]
Every donor, recipient, and intermediate physical capacity
in (8) remains. The other factors in (7) are the signed
physical crossings of \(W_*\), not further Euler stars.

For example, the actual reduced expression for the final
pointed source is still R's meromorphic Cartan trace
\[
 \Phi_{r+1}(W_{\rm fin})
   =\operatorname{Tr}_{r}
      \left(\frac{D_N(M)}{D_N(MK_{\rm r})}
                         \kappa S_rD_{\rm red}W_*\right),
 \qquad
 D_N(z)=\frac{z^N-z^{-N}}{z-z^{-1}}.
 \tag{9}
\]
Its continuation at completeness is the original removable
source. In particular its first meridian derivative is
the derivative of the actual family in (9), including the
Cartan kernel, \(S_r,D_{\rm red},W_*\), and \(\kappa\).
One does not differentiate only a root-level classical
identity or retain the old width in a newly reduced source.

## 3. At most three left stabilizations give a regular total

Now work at completeness with a non-elementary discrete
faithful knot-group representation. Let
\[
                H_1,\ldots,H_m,\qquad P=H_m\cdots H_1
 \tag{10}
\]
be its noncentral parabolic meridians in R/G's signed
convention. The tuple is a fixed point of the actual
Hurwitz braid word.

The inverse Hurwitz move sends an adjacent pair to
\[
                     (A,B)\longmapsto(B,BAB^{-1}).
 \tag{11}
\]
It preserves their ordered product \(BA\). Applying (11)
successively moves any chosen \(H_j\) to the first
position unchanged. Conjugate the actual braid by this
finite word. Its new fixed tuple has the same total \(P\).
This is one of the source-preserving conjugations in
Section 1.

Duplicate that first meridian in a left stabilization.
The new tuple is
\[
                  (H_j,H_j,\ldots)
 \tag{12}
\]
with the remaining entries those of the conjugated tuple.
The old word, embedded on the last heads, fixes its old
tuple; the new positive crossing fixes the equal pair.
Thus this is a fixed tuple of (3), and its new total is
\(PH_j\). Repeating the same left stabilization gives
\(PH_j^t\), with the actual integer \(t\), not a
continuously changed representation parameter.

Suppose first that \(P\) is noncentral parabolic. Write
\[
 P=\epsilon(I+U),\quad H_j=\delta(I+V),\quad
 U^2=V^2=0,\quad \epsilon,\delta\in\{1,-1\}.
 \tag{13}
\]
Irreducibility supplies a meridian whose fixed line
differs from that of \(P\). Then
\(\operatorname{tr}(UV)\ne0\): in a basis making \(U\)
strictly upper triangular, the lower-left entry of \(V\)
is nonzero and computes this trace. Therefore
\[
 \operatorname{tr}(PH_j^t)^2
             =\bigl(2+t\operatorname{tr}(UV)\bigr)^2 .
 \tag{14}
\]
For \(c\ne0\), \(2+c\) and \(2+2c\) cannot both belong
to \(\{2,-2\}\). One or two left stabilizations using
this chosen first meridian make the total regular
semisimple.

If \(P\) is central, one left stabilization makes it
noncentral parabolic. The enlarged tuple remains
irreducible. Choose a different meridian flag by
(11), and apply the preceding argument. This uses
at most three left stabilizations in total.

If the original \(P\) is already regular semisimple,
perform one left stabilization anyway, to ensure the
one-star form (6). Its total \(PH_j\) cannot be central:
otherwise \(P\) would be a scalar multiple of the
parabolic \(H_j^{-1}\). If it is regular, stop. If it
is noncentral parabolic, (11)--(14) need at most two
further left stabilizations. Again the total number
is at most three.

This proves the claimed bound in all cases. The tuple
always generates the same image group: Hurwitz moves
preserve that group and a stabilization only duplicates
a meridian. All intermediate words remain fixed finite
words, independently of \(N\). Although a conjugation
can introduce further index-one generators, the FINAL
left stabilization shifts the entire preceding word.
Thus (6)--(7) hold regardless of those earlier moves.

The resulting regular total is loxodromic. Indeed a
noncentral regular element of a torsion-free discrete
subgroup cannot be elliptic: a finite-order elliptic
is torsion, while powers of an infinite-order elliptic
accumulate at the identity.

## 4. The one donor is the actual resolved lower row

Let \(H\) be the duplicated first meridian in the FINAL
stabilization, \(v\) an eigenline of the resulting
loxodromic total, and \(w\) the selected eigenline of
\(H\). These lines are distinct. Otherwise a
loxodromic element and a nontrivial parabolic would
share a fixed point; conjugating the latter by
appropriate powers of the former would give distinct
group elements converging to the identity.

Use the basis \((v,w)\). At completeness \(x_{\rm cl}=-1\),
and the first two DRESSED meridians are the same matrix
\[
              H=\begin{pmatrix}x_{\rm cl}&0\\
                                    c&x_{\rm cl}^{-1}
                 \end{pmatrix},\qquad c\ne0 .
 \tag{15}
\]
The nonzero lower entry follows because \(v\) is not
the unique parabolic flag. The first lower Gauss
matrix and the second physical factor are therefore
\[
 b_{-,1}=\begin{pmatrix}1&0\\-c&x_{\rm cl}\end{pmatrix},
 \qquad
 G_2=b_{-,1}Hb_{-,1}^{-1}
     =\begin{pmatrix}x_{\rm cl}&0\\
                       c/x_{\rm cl}&x_{\rm cl}^{-1}
       \end{pmatrix}.
 \tag{16}
\]
Thus the second physical factor has
\[
 K_2=x_{\rm cl},\qquad A_2=1,\qquad
 p_2=0,\qquad f_2=c/x_{\rm cl}^{\,2}\ne0 .
 \tag{17}
\]
Here \(p_2=0\) specifies the selected flag, not an
arbitrary choice of a solution of a zero-product
equation. In the resolved chart of G,
\[
 A=1+pt,\qquad f=-t ,
 \tag{18}
\]
the point (17) has finite nonzero \(t\).

G's section of total lowering zero identifies the
remaining physical factors with the old factors
numbered \(2,\ldots,r+1\). The embedded \(W_*\)
returns the old tuple, so (17) is the donor entering
\(D_{\rm red}\) in (7). The principal map of that
diagonal factor is
\[
 A'=A,\qquad p'=-Ap/x_{\rm cl}^{\,2},\qquad
 f'=-x_{\rm cl}^{\,2}f/A .
 \tag{19}
\]
It therefore preserves \(A=1,p=0\) and the unit
condition on \(f\). This is the donor entering \(S_r\).

Equation (5) identifies the retained boundary at
this final crossing with old first occupation zero,
as well as new first occupation zero. This supplies
the lower local lift \(\log A=0\) for the duplicated
flagged donor. In the resolved chart it is the
initialized coherent boundary, not an upper
occupation sheet reset to zero. Rewriting the
same source as the full reduced trace (9) does
not assert that its other logarithmic sectors or
finite capacity terms have disappeared.

G also proves that every \(K_j,f_j\), and every
Euler denominator \(T_j\), is a unit on this
geometric resolved correspondence. The proof uses
the same loxodromic/parabolic disjointness for all
prefixes and reselected first flags. Its assumptions
now hold for the final presentation just constructed.

## 5. Recipient charts and the remaining analytic task

The presentation theorem supplies an exact initialized
DONOR; it does not require every recipient factorial
shape to be different from one. There is a precise
invariant reason for possible exceptions.

Every lower Gauss prefix fixes the second coordinate
line. In G's physical coordinates the selected flag
of a head is \([p_j:1]\). Consequently, at this
section,
\[
 p_j=0
 \quad\Longleftrightarrow\quad
 \text{its dressed meridian flag is the selected
       first-meridian flag}.
 \tag{20}
\]
Since \(f_j\) is a unit, \(A_j=1-p_jf_j\) makes this
equivalent to \(A_j=1\). Changing the eigenline
\(v\) of the total does not remove the flag
coincidence in (20).

Recipients satisfying (20) have the same resolved
factorial chart as (18), with
\(p_j=0,\ t_j=-f_j\ne0\) and the lower local germ
\(\log A_j=0\). This is a coordinate assignment,
not an elementary coherent-kernel asymptotic.
The other recipients have
\(p_j\ne0\) and \(A_j\ne1\), and are regular physical
spin-coherent candidates. This is a chart distinction,
not a permission to omit the factorial changes of
basis. A mixed choice must put each actual \(G_F\)
on both incident kernels and keep its finite
identity resolution.

In particular, the theorem alone supplies no
uniform weak-donor estimate with arbitrary physical
recipients, no compatible full-word contour, and
no estimate on any internal physical crossing.
Such estimates must concern the actual gauges and
the complete caps in (7)--(9). A local unit on the
initialized row also does not determine the
coefficient of its geometric normal cycle.

The useful conclusion is narrower and universal:
the need to initialize many unrelated Euler donors
can be removed by exact source-preserving
presentation changes. One positive initialized
Euler star, the original physical word, its
interfaces, and its actual pointed meridian
functional remain.

## Complete proof-source pins

* R: notes/research_actual_reduced_braid_source.md, 330 lines,
  SHA256 9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.
* G: notes/research_actual_reduced_braid_critical_scheme.md, 564 lines,
  SHA256 ddddcd9bf75f35afdf3e5de0c03323acee2c66e624db36142c2344ef729a977a.

Both complete sources were freshly read nontruncated in this
author sequence. The left trace, actual word order, finite
stabilization bound, and flagged donor calculation above
were checked from those complete sources and the displayed
finite formulas. No mathematical programs or tests were run.
Frozen and public files were not edited.
