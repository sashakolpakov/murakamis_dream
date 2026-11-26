# The full lower-left integral with a following three-twist block

Private research proof candidate, 8 November 2026. The estimates
for the first incoming path assemble to control the shared interval
\([0,11/50]+ih_y\) for a following type-three kernel, provided
\(|e^{-2\pi iy}|\le7/10\). The original filter and its denominator
are included. This extends the known nonzero lower-contour
contribution to the whole interval \([0,1/2]+ih_y\) on this
reference family.

Adoption requires the source and proof reviews of the new initial,
right-horizontal and corner inputs, and of this assembly.
The other signed contours remain unestimated here. No numerical
evaluation or change to a frozen proof is used.

## 1. Source, reference domain, and the incoming cycle

Keep the actual ordinary-next reference, original action
\(\mathcal P_0^+(w,z)\), and affine bound \(\Lambda_{123}(z)\)
of [the lower-central theorem](research_mixed_next_complete_lower_plateau.md),
with flags \((0,1,0)\). Both conditional vertices are ordinary.
Write
\[
\begin{gathered}
P=[11/50,9/20],\qquad J_L=[0,11/50],\\
y=q+ih_y,\quad q\in J_L,\qquad -.102<h_y<-.001,\\
z=u+ih_z,\quad u\in P,\qquad -.065<h_z<.068,\\
Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz},\qquad
13/25<R:=|Y|\le7/10 .
\end{gathered}
\tag{1}
\]
All heights and other reference data retain their original
correlations. At the actual output,
\[
\Lambda_{123}(z_*)=\Re\mathcal P_0^+(-2,z_*).
\tag{2}
\]
There is no outgoing halfweight for this next type.

For \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and
\(p_j(V)=(rV;r)_j\), let
\[
\begin{split}
C_{\beta,N}(V,W)&=\sum_{j=0}^{N-1}
             V^{-j}p_j(V)p_j(W)/P_j^{2+\beta},\\
F_N(w,Y)&=N\operatorname{CT}_X
                [U_{0,N}(w,X)C_{1,N}(X,Y)],\\
\mathscr D_{0,N}(w;y,z)&=F_N(w,Y)d_N(Y)C_{0,N}(Y,Z).
\end{split}
\tag{3}
\]
Here \(U_{0,N}\) is the complete original cap, and \(d_N\)
is the original polynomial of degree at most \(N-1\) with
\(d_N(r^b)=P_b^{-1}\). All finite sums retain their full ranges.

Use the original increasing incoming cycle
\[
\begin{split}
\Gamma_a={}&[0,1/10]\\
&{}\cup\{x+ih_a(x-1/10)/(3/25):1/10\le x\le11/50\}\\
&{}\cup[11/50+ih_a,9/20+ih_a]
 \cup[9/20+ih_a,1/2+ih_a]\\
&{}\cup[1/2+ih_a,1/2]\cup[1/2,1],
\qquad -.072<h_a<0 .
\end{split}
\tag{4}
\]
The finite Laurent integrand is entire in the logarithmic
coordinate \(a\), so its original constant-term identity is
\[
F_N(w,Y)=N\int_{\Gamma_a}
 U_{0,N}(w,e^{-2\pi ia})C_{1,N}(e^{-2\pi ia},Y)\,da .
\tag{5}
\]
The factor \(+N\) and the orientation have not changed.

## 2. The entire first integration

**Theorem 1.** On (1), for every real ordinary color \(w\in[-2,2]\)
and sufficiently large levels of either parity,
\[
\boxed{\quad
|\mathscr D_{0,N}(w;y,z)|
 \le CN^B e^{N\{\Lambda_{123}(z)-10^{-12}\}} .
\quad}
\tag{6}
\]

*Proof.* Each of the following estimates includes the same
complete product \(d_N(Y)C_{0,N}(Y,Z)\).

The [initial and taper theorem](research_mixed_next_three_deep_radius_incoming_initial_taper.md)
controls the first two parts of (4), with deficit \(10^{-12}\).
The [complete central theorem](research_mixed_next_own_three_deep_radius_complete_central.md)
controls the density on \(P+ih_a\), with deficit \(10^{-11}\).
The [right-horizontal theorem](research_mixed_next_three_deep_radius_right_horizontal.md)
controls the segment from \(9/20+ih_a\) to \(1/2+ih_a\),
also with deficit \(10^{-11}\). Integrating these pointwise
bounds costs only a bounded path length and a factor of \(N\).

Split the last real segment at \(7/10\).
The [corner theorem](research_mixed_next_three_deep_radius_incoming_corner.md)
controls the combined oriented path
\([1/2+ih_a,1/2]\cup[1/2,7/10]\), with deficit \(10^{-10}\).
Its replacement rectangle estimates the combined old path;
separate absolute bounds on the two old sides are unnecessary.

On the remaining segment \([7/10,1]\), equation (24) of
[the unselected right-tail theorem](research_mixed_next_unselected_incoming_right_tail.md)
bounds the complete preceding factor by
\[
 |U_{0,N}(w,X)C_{1,N}(X,Y)|
 \le CN^B e^{153N/100},\qquad |Y|\le1 .
\tag{7}
\]
This is a bound for the complete finite preceding product, with
all real ordinary colors. Since
\(153/100<2383/1500\), the
[type-three attachment theorem](research_mixed_next_three_deep_radius_bounded_prefix.md)
attaches the complete following factor on (1), with deficit
\(1/200\). It includes the endpoint and the original measure.

These pieces exhaust (4). Every following factor is independent
of \(a\), so the oriented integral bounds apply to (5) directly.
Adding their finitely many polynomial prefactors proves (6).
\(\square\)

## 3. Outside parameters and normalized derivatives

The derivative statement is proved after assembling (5).
No moving cut or deformed path is differentiated.

For fixed \(Y\), \(\mathscr D_{0,N}\) is a polynomial of degree
at most \(N-1\) in \(w\), and at most \(N-1\) in \(Z\).
Indeed the cap has that ordinary-color degree, constant-term
extraction does not increase it, and the outgoing dependence
comes entirely from \(C_{0,N}(Y,Z)\). Apply
[polynomial continuation from horizontal bounds](research_mixed_horizontal_complex_extension.md)
to (6). Its Chebyshev bound applies to \(w\in[-2,2]\), and
its logarithmic-arc bound to \(z\in P+ih_z\).
The degrees are linear in \(N\); the reference and \(q\)
are fixed compact labels. A sufficiently small fixed complex
neighborhood therefore costs any prescribed positive amount
in the exponential rate.

Using (2), continuity of the original holomorphic action,
and smaller neighborhoods at the actual output gives
\[
 |e^{-N\mathcal P_0^+(w,z)}
                 \mathscr D_{0,N}(w;y,z)|
 \le CN^B e^{-10^{-13}N}.
\tag{8}
\]
There is no outgoing weight to remove. Cauchy's formula on
smaller fixed neighborhoods gives every fixed mixed derivative.
In particular, for \(\gamma_L=J_L+ih_y\) and fixed \(j,k\ge0\),
\[
\partial_w^j\partial_z^k
\left[e^{-N\mathcal P_0^+(w,z)}
 N\int_{\gamma_L}\mathscr D_{0,N}(w;y,z)\,dy\right]
 =O_{j,k}(e^{-10^{-14}N}).
\tag{9}
\]
All reference heights, paths and cutoffs are fixed at the base
point before taking these derivatives. This is not a claim
that a varying geometric reference remains in (1) on a complex
neighborhood.

## 4. The unchanged filter and denominator

Keep the cardinal projection, first-node deletion, and \(11/12\)
cutoff of
[the complete lower-right shoulder theorem](research_mixed_next_complete_lower_right_shoulder.md),
Section 3:
\[
\begin{split}
F_N^{\rm mid}&=(I-\Pi)(F_N-R_N^{\rm node}),\\
E_N^{\rm filt}&=F_N-F_N^{\rm mid},\\
K_N(y)&=\frac{N F_N^{\rm mid}(w,Y)d_N(Y)C_{0,N}(Y,Z)}
                      {1-Y^N}.
\end{split}
\tag{10}
\]
The superscript distinguishes the finite correction
\(E_N^{\rm filt}\) from the canonical reciprocal factorial.
The established correction estimate is
\[
\sup_{|Y|\le1}|E_N^{\rm filt}(w,Y)|
       \le CN^B e^{77N/50},\qquad -2\le w\le2 .
\tag{11}
\]
Because \(77/50<2383/1500\), the type-three attachment theorem
applies on the new shared-variable interval as well. It gives
\[
|E_N^{\rm filt}(w,Y)d_N(Y)C_{0,N}(Y,Z)|
 \le CN^B e^{N\{\Lambda_{123}(z)-1/200\}}.
\tag{12}
\]
This verifies the correction's domain explicitly.

On \(\gamma_L\), \(|Y^N|\le(7/10)^N\), so
\(|1-Y^N|\ge1/2\) for all sufficiently large \(N\).
The exact difference is
\[
K_N-N\mathscr D_{0,N}
 =N\,\frac{Y^NF_N-E_N^{\rm filt}}{1-Y^N}
                      d_N(Y)C_{0,N}(Y,Z).
\tag{13}
\]
Its first term uses (6) and the extra factor \(|Y^N|\);
its second uses (12). The projection and deletion in (10)
are linear in \(Y\) and do not increase the ordinary-color
degree. The correction product has the same linear degree
bounds in \(w,Z\) as the original product.
Thus the continuation and Cauchy argument of Section 3
applies to both terms of (13); the denominator depends only
on the fixed integration variable. We obtain
\[
\boxed{\quad
\partial_w^j\partial_z^k
\left[e^{-N\mathcal P_0^+(w,z)}
                  \int_{\gamma_L}K_N(y)\,dy\right]
 =O_{j,k}(e^{-10^{-14}N}).
\quad}
\tag{14}
\]
Every original normalization and both Fourier alternatives
are retained.

## 5. The full lower-half contribution and the remaining signed contours

The existing lower-central and shoulder theorem, specialized
to next type three, gives
\[
N\int_{[11/50,1/2]+ih_y}\mathscr D_{0,N}(w;y,z)\,dy
 =N^{-2}\mathcal A_0(w,z)e^{N\mathcal P_0^+(w,z)}
                 (1+O_{\rm hol}(N^{-1})),\qquad \mathcal A_0\ne0 .
\tag{15}
\]
Adding (9) proves
\[
\boxed{\quad
N\int_{[0,1/2]+ih_y}\mathscr D_{0,N}(w;y,z)\,dy
 =N^{-2}\mathcal A_0(w,z)e^{N\mathcal P_0^+(w,z)}
                 (1+O_{\rm hol}(N^{-1})).
\quad}
\tag{16}
\]
The action, leading coefficient and power \(N^{-2}\) are
unchanged. This is a statement about the specified lower
integral, not an identification of that integral with a
complete Fourier coefficient.

The signed remainder in the shoulder theorem loses precisely
the lower-left term controlled by (14). For this reference
family the remaining expression is
\[
\mathscr R_N^{(3)}
 =\int_{[1/2,1]+ih_y}K_N(y)\,dy
 -\int_{[s,11/50]+iH}K_N(y)\,dy
 -\int_{[9/20,1-s]+iH}K_N(y)\,dy,\qquad H=1/100 .
\tag{17}
\]
The positive cutoff \(s\) is the same original upper seam
cutoff. Its sign conventions and all kernels are unchanged.
If \(\eta_{\rm old}>0\) is the previous error constant, set
\(\eta_{\rm new}=\tfrac12\min\{\eta_{\rm old},10^{-14}\}\).
The exact original transfer then satisfies
\[
\partial_w^j\partial_z^k
\left[e^{-N\mathcal P_0^+(w,z)}
 \{\mathcal T_0[F_N]-I_{\rm geom,N}-\mathscr R_N^{(3)}\}\right]
 =O_{j,k}(e^{-\eta_{\rm new}N}).
\tag{18}
\]
Here
\[
\mathcal T_0[F_N]
 =N[Y^0](F_Nd_NC_{0,N})+N[Y^N](F_Nd_NC_{0,N}),
\]
and \(I_{\rm geom,N}\) is the original local geometric integral
in the shoulder theorem. No contour or coefficient of that
integral is changed by (18).

Bounding the signed expression (17) at the required rate is
still necessary for the full transfer. The larger-radius
references and arbitrary fixed short compositions are also
outside this theorem. The finite-exception objective therefore
remains open.
