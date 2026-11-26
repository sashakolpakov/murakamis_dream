# A common physical tensor Krein form for the original crossings

Written research proof, 22 November 2026. The original complete crossing
preserves an explicit tensor product of one-head indefinite Hermitian
forms. The same form works on overlapping adjacent pairs at arbitrary
width. Its full change of coordinates to the prepared flags is proved
entrywise, including every cyclic endpoint. The ordinary cup and cap
are compatible with this form; the marked cap remains different.

The form is indefinite. These identities give neither a positive
whole-source norm nor a scalar noncancellation estimate. In particular,
they do not identify the actual paired-face wire with a Hermitian
pairing or remove any original pivot or marked boundary factor.

## 1. Original physical and flag conventions

Use the complete balanced physical heads of [D,W,P,C], with
\[
 N\geq2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad x=-q^{-1},\quad \lambda=x^{-1}=-q,\quad
 k=(-1)^d,\quad F_a=(Q;Q)_a .                         \tag{1}
\]
Physical indices lie in \(0,\ldots,d\); brackets mean cyclic reduction
to this set. Thus \(F_d=N\), \(\lambda^2=Q\), and \(\lambda^N=k\).
Every factorial denominator below has index at most \(d\).
Write \(Z|r\rangle=Q^r|r\rangle\) and
\(R_d|r\rangle=|d-r\rangle\). Define on one physical head
\[
 H_N=q^{-1}Z^{-1}R_d,\qquad
 H_N|r\rangle=qQ^r|d-r\rangle .                       \tag{2}
\]
Directly \(H_N^\dagger=H_N\) and \(H_N^2=I\). On two heads put
\[
 \mathcal K_N=-Nk(H_N\otimes H_N).
 \tag{3}
\]
It is Hermitian and \(\mathcal K_N^2=N^2I\).

Let \(\widetilde{\mathcal B}\) be the source-fixed invertible flag
frame of [D, (27)], with the wraps \(S_1^N=1,S_2^N=k\).
Its coordinates are \(|m,s\rangle\). Put \(a=[-s]\).
Expanding [D, (25),(27)] gives every physical coefficient:
\[
 \begin{split}
 \widetilde{\mathcal B}|m,s\rangle
   &=\sum_{h=0}^{a} A_{m,a,h}|[m+h],a-h\rangle,\\
 A_{m,a,h}
   &=\frac{(-1)^h\lambda^{a-h}
              Q^{ma+h(h+1)/2}}{F_hF_{a-h}} .
 \end{split}                                                   \tag{4}
\]
Indeed the diagonal rescaling in [D] is
\(\lambda^aQ^{ma}/F_a\), and \(\lambda^ax^h=\lambda^{a-h}\).
This uses the complete physical space, of dimension \(N^2\).

In these flag coordinates [D,W] give
\[
 \begin{gathered}
 v=Z_s,\qquad M=Z_m,\\
 X|m,s\rangle=(1-Q^{-m})(1-Q^{1-s})|m-1,s-1\rangle,
 \qquad X^N=0 .
 \end{gathered}                                                   \tag{5}
\]
Here \(X\) is the physical nilpotent crossing argument of [W], not
an additional boundary variable. Define the flag permutation and form
\[
 \mathcal R|m,s\rangle=|d-m,1-s\rangle,\qquad
 J=q\mathcal Rv^{-1}.
 \tag{6}
\]
All labels in (5),(6) are cyclic. Since
\(\mathcal Rv\mathcal R=Qv^{-1}\), one has
\(J^\dagger=J,J^2=I\), and
\[
 J_{ms;nt}=qQ^{-t}\delta_{m,d-n}\delta_{s,1-t}.
 \tag{7}
\]

## 2. Full physical congruence

The exact relation between the two forms is
\[
 \boxed{\quad
 \widetilde{\mathcal B}^{\dagger}\mathcal K_N
                   \widetilde{\mathcal B}=J .\quad}
 \tag{8}
\]
We prove all matrix entries. For a left label \((m,s)\) and a right
label \((n,t)\), put \(a=[-s],b=[-t]\), and \(R=a+b-d\).
If \(R<0\), (4) and physical complementation in (3) give zero.
Otherwise a possibly nonzero term must satisfy
\[
 h+g=R,\qquad m+n+R\equiv d\pmod N .                  \tag{9}
\]
Every \(g=0,\ldots,R\) is then valid, with \(h=R-g\): the bounds
\(R\leq a,b\) follow from \(a,b\leq d\). If the second condition
in (9) fails the whole entry is zero.

For completeness, the only factorial identities needed are
\[
 \overline{F_u}=(-1)^uQ^{-u(u+1)/2}F_u,\qquad
 F_uF_{d-u}=N(-1)^uQ^{u(u+1)/2}.                       \tag{10}
\]
The second follows by reversing the last \(u\) factors of \(F_d\).
In the entry under consideration, \((a-h)+(b-g)=d\), so (10)
applies without a zero factorial. Also
\[
 \mathcal K_N|r,j\rangle
       =-NkQ^{r+j+1}|d-r,d-j\rangle .                  \tag{11}
\]
Insert (4) into (11), conjugating the left coefficient. Applying
(10) to \(F_{a-h}F_{b-g}\) yields the following full entry:
\[
 -k\lambda^{d-2a}Q^{n+b+1-ma+nb+R}
 \sum_{g=0}^{R}
   \frac{(-1)^gQ^{g(g-1)/2}}{F_gF_{R-g}} .             \tag{12}
\]
For example the power \(Q^{R-g}\) in this simplification comes from
\(\lambda^{b-a+h-g}=\lambda^{d-2a}Q^{R-g}\); hence no wrap sign is
being suppressed. The sum in (12) is \((1;Q)_R/F_R\), by the finite
\(Q\)-binomial theorem. It vanishes for every \(R>0\).

When \(R=0\), (9) implies literally \(b=d-a,n=d-m\).
The exponent in front of the sum is
\((n+1)(b+1)-ma\equiv0\pmod N\), and
\[
 -k\lambda^{d-2a}=q^{-1}Q^{-a}=qQ^b .                 \tag{13}
\]
This is exactly (7), since \(t=[-b]\) and \(s=[1-t]\).
Thus (8) holds on every pair of basis vectors, including \(N=2\),
even levels, and composite levels.

Both forms in (8) are indefinite. When \(N\) is even their positive
and negative indices are both \(N^2/2\). When \(N\) is odd, those
indices are \((N^2-1)/2\) and \((N^2+1)/2\): directly (7) has trace
\(-1\). In particular (8) is not a positive Gram identity.

## 3. The original crossing and marked full function

Use the exact original stripped crossing factorization [W, (9)]:
\[
 \begin{gathered}
 W=\mathcal G\mathcal E_N(X),\qquad
 \mathcal E_N(X)=\sum_{h=0}^d X^h/F_h=P_N(X)^{-1},\\
 P_N(X)=\sum_{h=0}^d(-1)^hQ^{h(h-1)/2}X^h/F_h,\qquad
 \mathcal G=\sum_{j=1}^N g_jE_j(v),\quad
 g_j=(-1)^{j-1}Q^{j(j-1)/2},\quad g_N=1 .
 \end{gathered}                                                   \tag{14}
\]
The full positive crossing is \(\kappa W\), and its negative is
\(\kappa^{-1}W^{-1}\), with the original scalar retained.

Equation (5) gives \(\mathcal RX\mathcal R=X^\dagger\), including
the zero coefficients, and therefore
\[
 JXJ=QX^\dagger,\qquad
 \mathcal E_N(X)^\dagger=P_N(QX^\dagger)
                       =JP_N(X)J .                   \tag{15}
\]
The middle identity follows from the first formula in (10).
Reflection sends the marked label \(j\in\{1,\ldots,N\}\) to
\(N+1-j\); the elementary equality \(g_{N+1-j}=g_j\) shows
\([\mathcal G,J]=0\). Also \(\mathcal G^\dagger=\mathcal G^{-1}\).
Equations (14),(15) consequently prove
\[
 W^\dagger=JW^{-1}J,\qquad W^\dagger JW=J
 \quad\text{in flag coordinates}.                     \tag{16}
\]

The marked physical-root full function of [P, (3),(12)] is
\[
 F_v=\phi_N\sum_{j=1}^N E_j(v)/F_{j-1},\qquad
 \phi_N=\sqrt N\exp\!\left\{i\pi\left[
       \frac14-\frac{N+N^{-1}}{12}\right]\right\} .      \tag{17}
\]
Here the \(j=N\) value is the specified top mark, not the zero at
the bottom logarithmic mark. Formula (10) gives
\(F_{j-1}F_{N-j}=Ng_j\), and \(|\phi_N|^2=N\). Thus the eigenvalues
\(f_j=\phi_N/F_{j-1}\) satisfy
\(\overline{f_j}f_{N+1-j}=1\). Hence, with no omitted scalar,
\[
 F_v^\dagger=JF_v^{-1}J,\qquad F_v^\dagger JF_v=J .     \tag{18}
\]

## 4. Cyclic root marks and physical tensor assembly

For the determinant-normalized cyclic function of [D, (14)], denote
its two orientations by \(\mathfrak d_Q,\mathfrak d_{Q^{-1}}\).
Their anchored finite products imply
\[
 \mathfrak d_{Q^{-1}}(z)\mathfrak d_Q(Qz)=1 .           \tag{19}
\]
Indeed each factor \(1-Q^rz\), including \(r=0\), has total
exponent \(-d/N\) on the left, while the two central prefactors
give \((1-z^N)^{d/N}\). Continue this identity with its marks.

Put \(\mathcal C_t=\mathfrak d_Q(tv)\) on the nondegenerate marked
cover. When \(t\) and \(\bar t\) use conjugate-compatible paths
and roots from zero, (19) and the reflection of clock labels give
\[
 \mathcal C_t^\dagger=J\mathcal C_{\bar t}^{-1}J,
 \qquad \mathcal C_t^\dagger J\mathcal C_{\bar t}=J .   \tag{20}
\]
For real \(t\) with a self-compatible mark this is a \(J\)-isometry.
No unrelated choice of a norm root is licensed by (20); singular
Fermat values are not evaluated by separating inverse factors.

Conjugate the flat statements (16),(18),(20) by
\(\widetilde{\mathcal B}\) and use (8). In original physical
coordinates they read
\[
 \begin{gathered}
 W^\dagger(H_N\otimes H_N)W=H_N\otimes H_N,\\
 F_v^\dagger(H_N\otimes H_N)F_v=H_N\otimes H_N,\\
 \mathcal C_t^\dagger(H_N\otimes H_N)\mathcal C_{\bar t}
                         =H_N\otimes H_N .
 \end{gathered}                                                   \tag{21}
\]
The scalar \(-Nk\) cancels. At completeness \(|\kappa|=1\), as
fixed by the original crossing normalization [C, (15)]. Thus both
full signed crossings satisfy the first identity in (21).

For any width \(b\), set \(\mathscr H_b=H_N^{\otimes b}\). On every
adjacent pair use its actual signed crossing \(R_i^{\pm1}\).
Tensoring (21) with the untouched one-head forms proves
\[
 (R_i^{\pm1})^\dagger\mathscr H_bR_i^{\pm1}
       =\mathscr H_b,\qquad
 \mathcal W^\dagger\mathscr H_b\mathcal W=\mathscr H_b
 \tag{22}
\]
for every finite signed word \(\mathcal W\), including overlapping
pairs. No common positive flag frame or transition-norm estimate is
needed: \(H_N\) is the same physical one-head matrix on every wire.

## 5. Genuine ordinary turns and the retained marked closing

The actual cup and ordinary cap [D,C] are
\[
 p=N\sum_{a=0}^d x^{a-d}|a,d-a\rangle,\qquad
 \ell_o|a,b\rangle=\frac{x^a}{N}\delta_{a+b,d} .       \tag{23}
\]
The second formula uses \(x^{-a}Q^{-a}=x^a\).
On degree \(a+b=d\), \(H_N\otimes H_N\) acts by the literal
complementation \(|a,b\rangle\mapsto|d-a,d-b\rangle\), because
the phase in (11) before its scalar is \(Q^{d+1}=1\).
Conjugating the cup coefficients therefore proves, on the full space,
\[
 \boxed{\quad p^\dagger(H_N\otimes H_N)=N^2\ell_o,
 \qquad p^\dagger(H_N\otimes H_N)p=0 .\quad}           \tag{24}
\]
Both rows vanish off degree \(d\); on that degree their coefficient
is \(Nx^a\). The last equality is the original ordinary bubble
\(\ell_op=0\). Equivalently \(p/N\) and \(N\ell_o\) are dagger
compatible for this indefinite tensor form, with their actual order.

The averaged marked row is instead \(\ell_m|a,b\rangle=x^b/N^2\),
with \(\ell_mp=1\). Its exact flag row is
\((\ell_m\widetilde{\mathcal B})_{ms}=Q^{-ms}/N^2\), while
\(\widetilde{\mathcal B}^{-1}p=N^2|0,1\rangle\) [D, (29)].
It is not the ordinary row of (24). The original marked cap,
pivots, peripheral and framing lines remain attached to every
application; none is replaced by a Hermitian adjoint by definition.

This establishes a common indefinite structure for the original
crossings and ordinary turns at all levels. It does not make an
arbitrary planar source a positive norm square, identify a paired-face
seam, bound a general observed period below, or select a geometric
integration cycle. The isotropic nonzero cup in (24) already prevents
turning these identities into positive reflection by a change of basis.

## Complete proof sources and coverage

- [D] [Retained Pachner ratio and physical flags](research_retained_pachner_ratio_physical_flags.md), 365 lines, SHA-256 `650d25db94060e306464ae00ef92ceb1e51ba4bec53da2c15ee67a89113be21a`.
- [W] [Actual crossing flag Euler exchange](research_actual_crossing_flag_euler_exchange.md), 287 lines, SHA-256 `784a76132cf8116ec8afc5807e6bd98bb51178beb7f959b7ce3ab42e56eab6b5`.
- [P] [Marked full-Phi flag pentagon](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_marked_full_phi_flag_pentagon.md), 328 lines, SHA-256 `3052cef4a1d666253562c13ceaf6a9bc472baf7691f23d13e33bb3f8d6e9888f`.
- [C] [Actual Pascal coherent Gram](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_pascal_coherent_gram.md), 494 lines, SHA-256 `b6e6d697b4e21d30ca683f265b9c41170a0bee424d783169b2e0c70233dc889e`.

[Reflection-compatible original cap metrics](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_reflection_marked_boundary_metric.md),
233 lines, SHA-256 `709bb3ae0ca888ded92de5d1e6dd6a570901330636b0c969063cd790c442f8f3`,
and [the original reflection obstruction](original_reflection_gram_obstruction.md),
212 lines, SHA-256 `98263806bbbb5d69a9c595d0bba5e9a653063bc306c36f5b75bb482427e7ce85`,
are coverage only. They distinguish reflected positive circle forms,
genuine dual objects, and the failure of automatic positive source
reflection. The new full physical congruence (8) and the common tensor
identity (22) are consistent with those distinctions.
