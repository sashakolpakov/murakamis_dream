# A coherent cap bound through the full negative incoming depth

Research deduction, 8 November 2026. The existing half-face cap
contour, re-cut at private real part \(43/100\), gives a complete
finite-source upper bound throughout
\[
             1/2\le\Re a\le14/25,\qquad -9/125\le\Im a\le0.
\]
Every coherent contour profile decreases when the incoming height
is lowered from zero, and then decreases when its real part moves
to the right. All omitted physical rows keep their separately
proved positive half-face bounds.

Combined with the positive-row transport on the later strip, this
bounds the complete original cap below the same \(\widehat M\)
ceiling on the entire rectangle
\([1/2,33/50]+i[-9/125,0]\). It does not assign a dominant saddle
or nonzero asymptotic there. No following affine comparison,
numerical evaluation, or change to a frozen source is used.

## 1. One fixed, already proved cap atlas

Use the original complete polynomial and its specified interpolation:
\[
\begin{split}
 U_{0,N}(w,X)
 &=\sum_{j=0}^{N-1}H_N(w,r^{-j})p_j(X)/P_j,
                  \qquad X=e^{-2\pi ia},\\
 \mathscr A_N(e,a,w)
 &=D_N(e)^{-1}C_N(e,w)\Pi_N(a+e)/\Pi_N(a),\\
 \Psi(e,a)
 &=S(e)+J(a+e)-J(a)-i\pi ae .
\end{split}
\tag{1}
\]
At \(e=j/N\), the second line is exactly the corresponding
summand of the first. Every scalar, primitive and chirp is the
one in [the original outer-cap identity](research_mixed_cap_outer_contour_reduction.md).

The complete re-cut construction in Sections 2--3 of
[the real-arc cap upper theorem](research_mixed_real_arc_complete_cap_upper.md)
uses
\[
 \ell=\frac{27}{100},\qquad b=\frac{43}{100},\qquad
 H_-=\frac{11}{200},\quad H_+=\frac1{25},\qquad
 h_+=\Im e_+\in(-1/20,0).
\tag{2}
\]
Here \(e_+\) is the original half-face private critical point;
the symbol \(h_+\) in (2) denotes that fixed negative main height,
not the upper alias height \(H_+\).
At \(a=1/2\), each of the following five profiles has upper rate
at most the original half-face action \(M_{\rm half}\):
\[
\begin{array}{ll}
 \Re\Psi(E+ih_+,1/2),&\ell\le E\le b,\\
 \Re\Psi(\ell,1/2),\quad \Re\Psi(b,1/2),&\\
 \Re\Psi(E-iH_-,1/2)-2\pi H_-,&\ell\le E\le b,\\
 \Re\Psi(E+iH_+,1/2)-2\pi H_+,&\ell\le E\le b .
\end{array}
\tag{3}
\]
The real cuts have strict gaps, as do the horizontal aliases.

The complete endpoint coefficient and its all-real-color upper
bound hold on the entire original rectangle
\[
 [27/100,49/100]+i[-11/200,1/25].
\tag{4}
\]
Thus the new incoming rectangle does not require extending
\(C_N\) or identifying its saddle at negative incoming height.
The incoming factorial arguments stay uniformly regular:
\[
 \frac{77}{100}\le\Re(a+e)\le\frac{99}{100},\qquad
              \frac12\le\Re a\le\frac{14}{25}.
\tag{5}
\]
In particular no numerator period wall is crossed in this
retained contour.

## 2. Quantitative decrease of every fixed private profile

Write
\[
 a=\frac12+d-i\eta,\qquad
 0\le d\le\frac3{50},\quad0\le\eta\le\frac9{125},\qquad
 p=e^{2\pi ie},\quad R=e^{-2\pi\eta}.
\tag{6}
\]
As in the [positive-depth transport](research_mixed_cap_negative_depth_positive_transport.md),
\(5/8<R\le1\). The exact original multiplier is
\[
                    e^{\Psi_a(e,a)}
                    =\frac{1-X/p}{1-X}.
\tag{7}
\]

**Lemma 1.** At every fixed \(e=E+iH\) in the retained rectangle
\(\ell\le E\le b\), \(-H_-\le H\le H_+\),
\[
 \Re\Psi(e,1/2+d-i\eta)
 \le \Re\Psi(e,1/2)-\frac{\eta}{4}
                         -\log(12/11)\,d.
\tag{8}
\]

*Proof.* First fix \(d=0\). Since \(\sin\pi(1/2-i\eta)\)
is positive real, the original derivative has imaginary part
\[
 \Im\Psi_a
 =\arg\sin\pi(1/2+E+i(H-\eta))-\pi E.
\tag{9}
\]
The sine in (9) has positive real part and argument strictly
between \(-\pi E\) and \(\pi E\). Thus (9) is in
\((-2\pi E,0)\subset(-\pi,0)\). It is precisely the principal
argument of \((1+R/p)/(1+R)\) in (7), not a different logarithmic
lift.

For a quantitative bound put \(t=\pi E\) and
\(b_\eta=\tanh\pi(\eta-H)\). Then
\[
 b_\eta<\frac25,\qquad 1<\tan t<5.
\tag{10}
\]
Indeed \(\eta-H\le127/1000\),
\(127\pi/1000<2/5\), and \(\tanh s\le s\) for \(s\ge0\).
The upper tangent bound follows from
\(\tan(43\pi/100)=\cot(7\pi/100)<100/(7\pi)<5\).
The negative of (9) is \(t-\arctan(b_\eta\tan t)\).
If \(b_\eta<0\), it exceeds \(t>\pi/4\).
Otherwise, with \(s=\tan t\in[1,5]\), the exact tangent
subtraction formula gives
\[
\begin{split}
 t-\arctan(b_\eta\tan t)
 &=\arctan\frac{(1-b_\eta)s}{1+b_\eta s^2}\\
 &>\arctan\frac{(3/5)s}{1+(2/5)s^2}
 \ge\arctan\frac3{11}>\frac14.
\end{split}
\tag{11}
\]
The rational function has its minimum at an endpoint of
\([1,5]\), where its values are \(3/7\) and \(3/11\).
The final inequality follows from
\(\arctan(3/11)>3/11-9/1331=354/1331>1/4\).
Thus (9) is less than \(-1/4\), uniformly.
Since \(\partial_\eta\Re\Psi=\Im\Psi_a\), lowering the
incoming height gives the first decrease in (8).

Next keep \(\eta\) fixed and move \(d\) to the right.
The arguments in (7) satisfy
\[
 \arg X\in[22\pi/25,\pi],\qquad
 \arg p\in[27\pi/50,43\pi/50].
\]
Their difference lies in \([\pi/50,23\pi/50]\subset(0,\pi/2)\).
In particular
\[
 |1-X/p|^2<1+\frac{16}{9}R^2,\qquad
 |1-X|^2>1+R^2+\frac95R .
\tag{12}
\]
Here \(|p|^{-1}\le e^{2\pi/25}<4/3\), by
\(2\pi/25<\log(4/3)\).
The second bound uses
\(\cos(2\pi d)\ge\cos(3\pi/25)>9/10\);
for example \(3\pi/25<2/5\) and
\(\cos t\ge1-t^2/2\) suffice.
The difference between the denominator and numerator in
(12) is greater than
\[
       \frac95R-\frac79R^2
       \ge\frac{46}{45}R>\frac{23}{36}.
\]
Also the actual denominator \(|1-X|^2\) is at most four.
Hence
\[
                   |e^{\Psi_a}|^2<\frac{121}{144},
             \qquad \partial_d\Re\Psi<-\log(12/11).
\tag{13}
\]
Integrating proves (8). \(\square\)

The fixed alias penalties in (3) do not depend on \(a\).
Therefore (8) applies to all five original profiles with
the same decrease. This is an estimate before summing
currents, not an asserted ratio of signed cap values.

## 3. Every remaining current and every physical row

The entire retained rectangle has
\[
 -\Re\Psi_{ee}
       =-\Re S''(e)-\pi\Re\cot\pi(a+e)>0.
\tag{14}
\]
The first term is positive by the original endpoint Schur
identity on (4); the second is positive by (5), at every
height occurring here. Thus private vertical rates are convex.
Adding either linear alias penalty preserves this convexity.

Keep the main path at the fixed height \(h_+\) in (2).
Every unweighted join between a real cut and this main line
is bounded by its two endpoints. Every weighted vertical
alias half is bounded by its real-cut and horizontal-alias
endpoints. By (3), (8), all of them have rate at most
\[
               M_{\rm half}-\eta/4-\log(12/11)d.
\tag{15}
\]
Both horizontal aliases and the complete main line have
the same bound directly.

To spell out the exact finite inventory, put
\[
 L_N=\lceil N\ell\rceil,\quad K_N=\lceil Nb\rceil,\qquad
 \ell_N=(L_N-1/2)/N,\quad b_N=(K_N-1/2)/N .
\tag{16}
\]
Apply the original counterclockwise cotangent-residue identity
to the complete interpolant \(\mathscr A_N\) for
\(L_N\le j<K_N\). The two constant halves give the density
\(+N\) on the real zero mode. There are exactly two horizontal
weighted currents, four vertical weighted half-currents and
two unweighted joins when that real zero mode is moved to
height \(h_+\). Every one is bounded above as just described.
The original endpoint coefficient is complete, and the
regular factorial chart is valid by (4)--(5). Half-grid shifts
are absorbed in an arbitrary common tolerance on fixed
neighborhoods. No numerator or Fourier kernel is divided out.

It remains to retain all physical rows outside (16).
For \(e=j/N\) in a compact physical interval, their entire
rate is \(\lambda(e)+I_{x,R}(e)\). The exact radial bound
\[
 I_{x,R}(e)\le-J(1/2-e)\quad(e\le1/2),\qquad
 I_{x,R}(e)\le J(e)\quad(e\ge1/2)
\tag{17}
\]
holds for every \(x\ge1/2\), \(R\le1\), as proved in
[far-half radial transport](research_mixed_three_four_far_half_cap_radial_extension.md).
In particular the rows beyond the real numerator wall
remain in (17).

Put \(\phi(e)=\lambda(e)-J(1/2-e)\).
The same real-half-face re-cut proof cited in Section 1 gives
\[
 \phi(e)\le \phi(\ell)<M_{\rm half}\quad(0<e\le\ell),\qquad
 \phi(e)\le \phi(b)<M_{\rm half}\quad(b\le e<1/2).
\tag{18}
\]
It proves both derivative signs and real concavity, so (18)
holds on the whole physical tails, not only at the cuts.
The upper half has rate at most \(b_0=101/125<M_{\rm half}\).
The two true private ends have their separate uniform
closed-disk rate \(3/5<M_{\rm half}\), from
[all-real complementary completion, Section 2](research_mixed_three_four_complementary_real_colors.md).
These source bounds include all real ordinary colors and
both parities. Define the fixed constant
\[
 B_{\rm tail}
   =\max\{\phi(\ell),\phi(b),101/125,3/5\}<M_{\rm half}.
\tag{19}
\]
This accounts for every omitted physical row.

## 4. Complete-source theorem and full-rectangle consequence

**Theorem 2.** Uniformly for
\[
 a=x-i\eta,\quad1/2\le x\le14/25,\quad0\le\eta\le9/125,
 \qquad w\in[-2,2],
\]
both parities and every \(\tau>0\) satisfy
\[
 |U_{0,N}(w,e^{-2\pi ia})|
 \le C_\tau N^{B_\tau}
 \exp N\left[
 \max\{M_{\rm half}-\eta/4-\log(12/11)(x-1/2),
                                  B_{\rm tail}\}+\tau\right].
\tag{20}
\]
All factors and currents are the original finite source.

The all-real claim uses the established upper bound for each whole
\(C_N(e,w)\) on (4) by its complete-color rate. Its angular gain
may be dropped. No remote-color saddle or new nonzero coefficient
is assigned. The sourcewise bounds in (3), (18) and the true-end
bounds retain this same all-real scope.

Combining (20) with
[the complete positive-row strip theorem](research_mixed_cap_negative_depth_positive_transport.md)
gives a fixed \(\gamma>0\) such that
\[
 \boxed{\quad
 \sup_{-2\le w\le2}|U_{0,N}(w,e^{-2\pi ia})|
       \le C_\tau N^{B_\tau}e^{N(\widehat M-\gamma+\tau)},
 \qquad a\in[1/2,33/50]+i[-9/125,0],
 \quad}
\tag{21}
\]
where
\[
                    \widehat M=\frac{203}{200}
                                      -\frac{1303}{7680000}.
\]
Indeed (20) has upper rate at most \(M_{\rm half}<\widehat M\)
on the first subrectangle; the positive-row theorem has a fixed
strict reserve on the second, including the common boundary
\(x=14/25\). No unquantified neighborhood is used to cover the
negative depth.

Fixed ordinary derivatives follow from the whole polynomial
all-real bound by Markov, with polynomial costs. For any
prescribed extra tolerance the original complex-color source
bounds yield a sufficiently small fixed neighborhood of complete
color. At each base incoming point keep the cuts and all paths
fixed. The factorial arguments in (5) have fixed strip margins;
the finite products and their zero-safe upper rates persist on
fixed neighborhoods. Cauchy on radius \(1/N\) then gives fixed
mixed incoming/ordinary derivatives with polynomial losses.
The positive-row part has the same local extension from its
own theorem. No moving index set is differentiated.

This is a complete upper bound on the actual required depth
rectangle. It neither encloses the cap saddle there in the
endpoint source domain nor proves a relative cap asymptotic.
Its use in an incoming contour deformation still requires the
full conditional factors, selected weights, and comparison
with their original correlated following affine action.

