# Independent calculation of the normalized ordered collar operator

1 November 2026. This records a local algebraic check. It does not assert
a global preferred-longitude formula.

Let \(A,B\in\mathrm{SL}_2(\mathbb C)\) have equal trace, and set
\[
 P=BA,\qquad K=P^{-1}-I,\qquad \delta=\det K\ne0.
\]
The actual positive ordered convention is
\[
 (A,B)\longmapsto(A^{-1}BA,A).
 \tag{1}
\]
This is the convention of equation (5.2) in
/Users/sasha/volume-conjecture/notes/marked_braid_holonomy.md.
Its two strand paths carry the ordered input vectors \((a,b)\) to
\((A^{-1}b,a)\).

## 1. Algebra without eigenframes

Cayley--Hamilton and equality of the traces give
\[
 KB=AK,\quad KAK^{-1}=A^{-1}BA,\quad
 K^2=-\delta P^{-1},\quad K^{-2}=-P/\delta.
 \tag{2}
\]
Consequently the operator
\[
 \mathcal B=\delta(K^{-1}A^{-1}\otimes K^{-1})\,\mathsf{s}
 \tag{3}
\]
has square
\[
 \begin{aligned}
 \mathcal B^2
 &=\delta^2(K^{-1}A^{-1}K^{-1})
       \otimes(K^{-2}A^{-1})\\
 &=\delta^2(-A/\delta)\otimes(-B/\delta)
 =A\otimes B .
 \end{aligned}
 \tag{4}
\]
Here \(\mathsf{s}\) interchanges the two tensor factors. The order in
(4) is essential. In particular the first factor is not
\(K^{-2}A^{-1}\).

The operator exchanges the two eigenvalue labels:
\[
 \mathcal B(A\otimes I)=(I\otimes B)\mathcal B,\qquad
 \mathcal B(I\otimes B)=(A\otimes I)\mathcal B.
 \tag{5}
\]
It is equivariant under a common conjugation of \(A,B\). It is regular
where \(\delta\) is a unit, including the noncentral parabolic point.
All its integer powers follow from (4), since it is invertible.

## 2. The four states and the parabolic limit

In a common vector basis write
\[
 A=\begin{pmatrix}\lambda&\alpha\\0&\lambda^{-1}\end{pmatrix},
 \qquad
 B=\begin{pmatrix}\lambda^{-1}&0\\\beta&\lambda\end{pmatrix}.
 \tag{6}
\]
Then \(\delta=-\alpha\beta\). In the ambient tensor basis
\((e_1e_1,e_1e_2,e_2e_1,e_2e_2)\), direct substitution in (3) gives
\[
 \mathcal B=
 \begin{pmatrix}
 0&0&0&-\alpha/(\beta\lambda)\\
 0&-\lambda&0&-\alpha\\
 0&0&-\lambda^{-1}&0\\
 -\beta\lambda/\alpha&0&-\beta&0
 \end{pmatrix}.
 \tag{7}
\]
This expression has no denominator \(\lambda-\lambda^{-1}\).

Put \(h=\lambda-\lambda^{-1}\) and use the eigenvectors
\[
 a_+=(1,0)^t,\quad a_-=(-\alpha,h)^t,\qquad
 b_+=(0,1)^t,\quad b_-=(h,-\beta)^t.
\]
For \(h\ne0\), equation (7) gives
\[
 \begin{aligned}
 \mathcal B(a_+\otimes b_+)&=-\lambda\,a_+\otimes b_+,\\
 \mathcal B(a_-\otimes b_-)&=-\lambda^{-1}a_-\otimes b_-,\\
 \mathcal B(a_+\otimes b_-)&=
       -\frac{\lambda\beta}{\alpha}a_-\otimes b_+,\\
 \mathcal B(a_-\otimes b_+)&=
       -\frac{\alpha}{\lambda\beta}a_+\otimes b_- .
 \end{aligned}
 \tag{8}
\]
The two mixed coefficients multiply to one. The mixed states are
exchanged, not multiplied separately by the equal-state coefficient.
The eigenframes degenerate at \(h=0\), but (7) remains regular. These
identities were also checked by direct symbolic multiplication,
including both relations in (5); the displayed derivations are the
proof.

## 3. What normalization (3) means geometrically

The unnormalized actual strand transport is
\((A^{-1}\otimes I)\mathsf{s}\). The outgoing representation is
identified with the incoming one by the common projective map \(K^{-1}\).
Choose either determinant-one lift
\(\widehat K=K/\sqrt{\delta}\). Applying
\(\widehat K^{-1}\) to both outgoing vectors gives exactly (3).
Changing the common square-root sign affects both vectors and hence
does not change their tensor. This explains the factor \(\delta\);
it is not an additional asserted knot normalization.

Replacing \(K\) by \(cK\) leaves (3) unchanged provided
\(\delta\) is, as defined, recomputed as \(\det(cK)\).
Thus (3) records the normalized two-path comparison intrinsically.
It does not identify the actual selected input eigenlines by itself.

## 4. Comparison with the native collar words

The native determinant-one punctures are
\((A_g,B_g,C_g,D_g)\), with product one. The pure boundary tables are
\[
 \begin{array}{c|c|c|c}
 &\text{input }(a,b)&\text{output }(a',b')&C_0\\ \hline
 v&(B_g,A_g)&(C_g^{-1},D_g^{-1})&S_v^{-1}\\
 w&(B_g^{-1},C_g^{-1})&(A_g,D_g)&S_w^{-1}.
 \end{array}
 \tag{9}
\]
They follow from the actual six white/shaded returns. Both rows
intertwine the two generators, not merely their traces, and preserve
\(P=ba=b'a'\). Therefore \(C_0K\), with \(K=P^{-1}-I\)
in the input frame, implements the actual positive collar (1).
Its sign agrees with the full \(M=1\) positive-collar matrix calibration.

The geometric ideal flags on a native disk side have opposite
selections. Formula (8), rather than the equal-state specialization,
is the appropriate raw bookkeeping. Alternatively one may explicitly
reverse one oriented strand path and switch its selected eigenline;
its transport coefficient is unchanged in determinant-normalized
eigenframes. That operation can turn a raw opposite pair into an
equal-selected pair, but a closed calculation must still cancel the
new endpoint frames consistently.

The corrected sewing construction first glues the full boundary
representations by (9) and (1), and then decorates the resulting
original group representation by its actual positive-main-meridian
eigenflags. That construction respects the necessary Weyl exchange.
It rebuilds the triangle maps rather than retaining the known
incorrect fixed-white odd chart. It gives a local decorated
representation. A global preferred-longitude product still requires
the original closed path and framing calculation.

## 5. Source references and a transcription correction

The reviewed inputs are
/private/tmp/md-decorated-hurwitz-line-transport.md and
/private/tmp/md-nonparabolic-pure-pages-and-hurwitz-collar.md.
In the former, equation (15) initially contained commas immediately
after three scalar coefficients. They mean multiplication and should
be replaced by ordinary TeX spacing. No algebraic correction is needed.
