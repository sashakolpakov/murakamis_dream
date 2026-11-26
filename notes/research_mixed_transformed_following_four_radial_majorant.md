# Outgoing-radius gains for the complete transformed remainder

Research deduction, 7 November 2026. The full complementary incoming
contour of the retained three/four prefix has a quantitative gain on
every outgoing disk strictly inside the unit circle. This supplies a
uniform finite-source bound on both actual type-four output enclosures.
It does not identify their context-dependent geometric action with
the action at the original pair's private leg.

## 1. The same complete finite source and incoming path

Keep the exact functions and normalization of
[the transformed complement](research_mixed_three_four_transformed_complement.md):
\[
\begin{split}
 r&=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\\
 U_{0,N}(w,X)&=\sum_{j<N}H_N(w,r^{-j})p_j(X)/P_j,\\
 C_{1,N}(X,Y)&=\sum_{j<N}X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 f_{+,N}(w,Y)&=N\int_{\Gamma_+}U_{0,N}(w,e^{-2\pi ia})
                           C_{1,N}(e^{-2\pi ia},Y)\,da,\\
 \Gamma_+&:[1/2+ic,1/2]\cup[1/2,1],
                   \qquad -7/200<c<0 .
\end{split}                                                     \tag{1}
\]
The fixed value \(c\) remains that of the original pair, as certified
by the already completed enclosure. It is a legitimate fixed
deformation of the polynomial contour for every outgoing \(Y\).
No new critical point or action is evaluated.

Put
\[
\begin{split}
 C_+&=\frac{17539}{9600},\qquad
 \beta(R)=\frac12\log\frac{2}{1+R^2},\quad 0\le R\le1,\\
 \mathfrak C(R)&=
 C_+-\frac{23}{64000}-\frac6{25}\beta(R)
                              +\frac{\beta(R)^2}{20}.
\end{split}                                                     \tag{2}
\]

**Theorem 1.** For every fixed \(0<R\le1\), every \(\tau>0\),
and every fixed \(k,\ell\), the complete source satisfies
\[
 \sup_{\substack{w\in[-2,2]\\ |Y|\le R}}
 |\partial_w^k\partial_Y^\ell f_{+,N}(w,Y)|
 \le C_{R,\tau,k,\ell}N^{B_{k,\ell}}
                        e^{N(\mathfrak C(R)+\tau)} .
                                                               \tag{3}
\]
The same bound holds near \(w=-2\) on a sufficiently small fixed
complex disk, on a smaller disk for derivatives. Both parities,
the entire incoming vertical segment, all physical transform rows,
and all numerator zeros remain included. The constants and color
neighborhoods can be chosen uniformly when \(R\) ranges in a fixed
compact subset of \((0,1]\). In particular
\[
 \mathfrak C(R)
 \le C_+-\frac{23}{64000}-\frac{89}{400}\beta(R)
 \le C_+-\frac{\beta(R)}5 .
                                                               \tag{4}
\]
The first inequality is strict for \(R<1\). The dependence on
the outgoing radius is an actual improvement of the whole finite
remainder estimate, not a comparison of signed source values.

## 2. The outgoing numerator retains a radius debit

Write
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\qquad
 L(t)=-2J((1-t)/2),\qquad
 I_Y(t)=\int_0^t\log|1-Ye^{-2\pi iu}|\,du .
                                                               \tag{5}
\]
The centered-arc comparison in
[the calibrated transformed remainder](research_mixed_three_four_transformed_complement_calibration.md),
equations (8)--(9), gives for \(t\le1/2\)
\[
 I_Y(t)\le L(t)-\beta(R)t,\qquad |Y|\le R\le1.
                                                               \tag{6}
\]
Indeed the maximizing arc for radius \(\rho=|Y|\) is centered
opposite \(1\). On that arc, with \(|u|\le t/2\le1/4\),
\[
 \frac{|1+\rho e^{2\pi iu}|^2}{|1+e^{2\pi iu}|^2}
  =\rho+\frac{(1-\rho)^2}{4\cos^2\pi u}
  \le\frac{1+\rho^2}{2}\le\frac{1+R^2}{2}.
                                                               \tag{7}
\]
Integration proves (6), including \(\rho=0\).
For \(t\ge1/2\) use the original whole-disk bound \(I_Y(t)\le L(t)\).
No numerator polynomial is divided at a zero.

For the lower-half rows define
\[
 D(t)=L(t)-J(1/2-t)-3J(t),\qquad 0\le t\le1/2.
                                                               \tag{8}
\]
The written scalar proof in the same source gives
\[
\begin{split}
 D''(t)&\le-2\pi\sqrt3,\qquad
 -1/10<D'(1/4)<0,\\
 D(1/4)&<d_0:=7/40-3/512+73/125 .
\end{split}                                                     \tag{9}
\]
These are analytic inequalities already proved with their original
constant; an upper bound for the whole source is not inverted to
deduce (9).

The supporting quadratic at \(1/4\), maximized on the real line,
therefore yields, for \(0\le\beta\le(\log2)/2<7/20\),
\[
\begin{split}
 \max_{0\le t\le1/2}[D(t)-\beta t]
 &<d_0-\frac\beta4+\frac{(1/10+\beta)^2}{20}\\
 &=\frac{377}{500}-\frac{23}{64000}
                 -\frac6{25}\beta+\frac{\beta^2}{20}.
\end{split}                                                     \tag{10}
\]
Here \(4\pi\sqrt3>20\). Since
\(\beta^2/20\le(7/400)\beta\), equation (10) also proves
the linear debit in (4).

## 3. Keep the complete vertical connector and upper rows

The complete first cap on \(\Gamma_+\) has rate
\[
                         B_0=1549/1500.
                                                               \tag{11}
\]
This is the whole coherent cap bound used in the original
transformed-complement theorem, uniformly for all real ordinary
colors and after fixed ordinary derivatives.

On the real part of \(\Gamma_+\), equation (10) directly bounds
the lower-half conditional rows after adding \(B_0\).
On the vertical part write \(\delta=-2\pi\Im a<11/50\).
The exact radial identity, with the incoming chirp retained, gives
\[
 D_\delta(t)-D(t)<\frac{11}{300}+\frac7{1920}
                          \quad(0\le t\le1/3),
 \qquad D_\delta'(t)<-1/3\quad(1/3\le t\le1/2).
                                                               \tag{12}
\]
These are the original complete-connector inequalities recorded in
Section 2 of
[the calibrated transformed remainder](research_mixed_three_four_transformed_complement_calibration.md),
with its original radial-identity and chirp source citations.
Subtracting \(\beta t\) preserves the second inequality.
Its maximum on the last interval is therefore at \(1/3\),
where the first inequality applies. Consequently all lower-half
rows on the full path have rate below
\[
 B_0+\frac{11}{300}+\frac7{1920}
 +\frac{377}{500}-\frac{23}{64000}
              -\frac6{25}\beta+\frac{\beta^2}{20}
                         =\mathfrak C(R).               \tag{13}
\]

The original upper-half estimate, including \(j=N-1\), has rate
at most \(793/500\). It remains valid on every smaller outgoing
disk. This is less than \(\mathfrak C(R)\) throughout
\(0\le R\le1\): from \(C_+>9/5\), \(23/64000<1/2000\),
and \(\beta<7/20\), one has
\[
 \mathfrak C(R)>
       \frac95-\frac1{2000}-\frac{21}{250}
       =\frac{3431}{2000}>\frac{17}{10}>\frac{793}{500}.
                                                               \tag{14}
\]
Thus no upper row has been dropped to obtain the radius gain.

Uniform zero-safe numerator upper estimates and the denominator
sine-factorial estimates now prove (3) for values. Allocate the
finite rate tolerances before choosing parameter neighborhoods.
For \(w\), apply the original positive-row Markov estimate to the
complete coherent coefficients before summing.
For outgoing derivatives, the polynomial degree is less than \(N\).
The disk growth inequality from radius \(R\) to \(R(1+1/N)\)
costs at most \((1+1/N)^{N-1}\le e\); Cauchy disks of radius
\(R/N\) therefore cost only fixed powers of \(N\).
The same argument applies to the complete integrated polynomial.
The cap's original complex-color estimates, or polynomial strip
growth with an allotted tolerance, give the fixed disk near
\(w=-2\). This proves every assertion of Theorem 1.

## 4. Actual type-four following domains

The exact reference-role theorem
[for ordinary last rows](research_mixed_actual_last_row_reference_domains.md)
defines
\[
\begin{split}
 O_4&=P_4\cap\{-51/500\le\Im z\le-1/1000\},\\
 A_4&=P_4\cap\bigl([123/500,7/20]
                          +i[-27/250,-1/50]\bigr).
\end{split}                                                     \tag{15}
\]
Actual ordinary outputs belong to \(O_4\); attached type-four
endpoint inputs belong to \(A_4\), with the roles and correlations
specified by that source. A private endpoint leg is not silently
substituted for an ordinary output.

All points of these two sets have \(h=\Im z<0\) and
\[
                 1/2<e^{2\pi h}<1.
                                                               \tag{16}
\]
The lower radius guard follows from \(h\ge-27/250\) and
the elementary exponential comparison already used in the
right-tail theorem. For \(s=-h\), direct differentiation gives
\[
 \frac d{ds}\beta(e^{-2\pi s})
      =\frac{2\pi e^{-4\pi s}}{1+e^{-4\pi s}}
                         >\frac{2\pi}{5}
                    \quad(0\le s\le27/250).
                                                               \tag{17}
\]
Integrating from zero, and applying (4), proves the explicit
context-independent source debit
\[
 \mathfrak C(e^{2\pi h})
 <C_+-\frac{\beta(e^{2\pi h})}{5}
 <C_+-\frac{2\pi}{25}(-h)
 <C_+-\frac6{25}(-h).                                  \tag{18}
\]
For example the entire ordinary enclosure has the uniform ceiling
\(C_+-3/12500\), and the attached enclosure has
\(C_+-3/625\), before an arbitrarily small prescribed tolerance.
The sharper function (2), rather than these coarser uniform
ceilings, can be retained at the actual output selected by a context.

The complete real initial interval also has a domain-independent
bound here: [the initial-interval theorem](research_mixed_transformed_real_initial_interval.md)
gives rate \(7/4\) for its entire \(N\)-integral, for all
\(|Y|\le1\), every real ordinary color, both parities and all
fixed derivatives. Thus neither the seam nor the complementary
contour requires a new source representation on (15).

## 5. The remaining calibrated comparison is explicit

Suppose an actual further attachment selects \(z\) in (15) and
its original pre-Gram prefix action is \(\mathcal P_{\rm ctx}(z)\).
For these two source pieces the precise sufficient comparison is
\[
 \Re\mathcal P_{\rm ctx}(z)>
       \max\{\,7/4,\ \mathfrak C(e^{2\pi\Im z})\,\}.
                                                               \tag{19}
\]
On a compact actual-reference family, a uniform positive margin
in (19) gives a uniform exponential bound for these complete
remainders after normalization; Cauchy's formula supplies fixed
mixed jets on any corresponding ambient source neighborhoods.
No sign of (19) throughout (15) is asserted here. In particular
\(\mathcal P_{\rm ctx}\) cannot be replaced by the post-Gram
phase \(H_{34}\), or by the complete pair action including its
removed endpoint.

The central plateau, left-taper anchors and right-strip anchors at
the context-selected output require their own pointwise comparisons.
The final Gram contraction and the full later factor
\(d_N(Y)(1+Y^{-N})\), with both original moduli, remain in that
next exact observation. This theorem supplies an improved complete
source bound on the genuine type-four domains; it does not infer
arbitrary short-component closure from the original private reference.
