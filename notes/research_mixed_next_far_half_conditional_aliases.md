# The conditional sum on the remaining real arc

Research deduction, 7 November 2026. The two end ranges of the
conditional sum have already been bounded below the selected geometric
action. For the retained rows, this note bounds every error in replacing
the finite sum by its real integral: both horizontal Fourier remainders
and the full vertical remainders at both cuts. The proof uses the exact
factorial interpolation and elementary argument bounds. It does not
estimate the remaining real integral.

The position of the main integral matters. Here it stays on the real
axis. A subsequent deformation of that integral must retain its own
connecting segments; the estimates below do not discard those segments.

## 1. The retained finite source and its regular phase

Use the source, constants, and cuts of
[the two end-range theorem](research_mixed_next_selected_first_wall_rows.md).
In particular,
\[
 \begin{gathered}
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\\
 \frac12\le a\le\frac{13}{16},\qquad X=e^{-2\pi ia},\\
 y=x+i/100,\quad x\in P=[11/50,9/20],\qquad
                         Y=e^{-2\pi iy},\\
 L_N=\lfloor N/16\rfloor+1,\quad
 K_N(a)=\lceil N(1-a-\varepsilon)\rceil,\\
 \ell_N=(L_N-1/2)/N,\qquad u_N=(K_N(a)-1/2)/N .
 \end{gathered}                                                   \tag{1}
\]
The fixed positive \(\varepsilon\) is the one obtained in that theorem.
For all sufficiently large \(N\), the real interval
\([\ell_N,u_N]\) lies in \([1/20,1/2)\), and
\[
 \frac12<a+t<1-3\varepsilon/4,\qquad
            0<x+t<19/20\qquad(\ell_N\le t\le u_N).
                                                                  \tag{2}
\]
Its lower and upper cuts are in the paid real collars.

Let \(\Pi_N\) be the original negative-root factorial interpolation
and \(E_N=1/\Pi_N\) in its regular strip. Keep its exact normalization.
The retained sum is
\[
 \begin{split}
 C_N^{\mathrm{mid}}(X,Y)
     &=\sum_{j=L_N}^{K_N(a)-1}
                  X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 T_N(s;a,y)
     &=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(y+s)
                         E_N(a)E_N(y)E_N(s)^3.
 \end{split}                                                     \tag{3}
\]
The factorial recurrence gives equality between the summand and
\(T_N(j/N;a,y)\) at every retained index. Equation (2) places every
factor in its regular strip throughout the rectangle
\[
              \ell_N\le\Re s\le u_N,\qquad |\Im s|\le2.
                                                                  \tag{4}
\]
In particular no numerator is continued through its positive real
wall in this rectangle.

On these strips use the original analytic primitive \(g\), with
\[
                 g'(z)=\Log(1-e^{-2\pi iz}).
                                                                  \tag{5}
\]
The branch in (5) is principal for \(0<\Re z<1\).
The phase of the exact interpolation (3) is
\[
 Q(s;a,y)=g(a+s)+g(y+s)-3g(s)-g(a)-g(y)+2\pi ias.
                                                                  \tag{6}
\]
The uniform factorial expansion on the fixed compact strips in (4)
therefore gives a polynomial prefactor times \(e^{N\Re Q}\).
For every tolerance \(\tau>0\), all uses below can be made with
an additional \(N\tau\) in the exponent, uniformly in the stated
parameters. No phase is substituted for a finite sum until this
interpolation and its bounds have been specified.

## 2. Argument bounds on both halves of the rectangle

Write
\[
 A(z)=\arg(1-e^{-2\pi iz}),\qquad s=t+ih .
                                                                  \tag{7}
\]
For \(0<\xi<1/2\), \(A(\xi+i\eta)\) lies between \(0\)
and \(\pi-2\pi\xi\); for \(1/2<\xi<1\), it lies between
\(\pi-2\pi\xi\) and \(0\). These statements hold for every
real \(\eta\). They follow by varying the positive radius in
\(1-R e^{-2\pi i\xi}\), whose imaginary part has fixed sign.
Differentiating (6) gives
\[
 \partial_h\Re Q(t+ih;a,y)
   =-A(a+t+ih)-A(y+t+ih)+3A(t+ih)-2\pi a.
                                                                  \tag{8}
\]

For \(h\ge0\), the same argument intervals, together with
\(a+t>1/2\), imply
\[
 \begin{split}
 \partial_h\Re Q
 &\le 2\pi-4\pi t+\max\{2\pi(x+t)-\pi,0\}\\
 &=\max\{2\pi-4\pi t,\ \pi+2\pi x-2\pi t\}
 \le \frac{9\pi}{5}.
 \end{split}                                                     \tag{9}
\]
The last step uses \(t\ge1/20\) and \(x\le9/20\).

For \(h\le0\) we need a sharper bound on only the second argument
in (8). Its real part satisfies \(x+t\ge27/100\), and its
height is at most \(1/100\). If \(x+t\ge1/2\), this argument is
nonpositive. Otherwise put
\[
 \theta=2\pi(x+t)\in[27\pi/50,\pi],\qquad
                     R=e^{2\pi(h+1/100)} .
\]
Here
\[
 R\le e^{\pi/50}<\frac{175}{164},\qquad
 \sin\theta+\cos\theta
       \le1-\sin(\pi/25)\le\frac{23}{25}.
                                                                  \tag{10}
\]
For the first inequality use \(\pi<22/7\) and
\(e^u<(1-u)^{-1}\) for \(0<u<1\).
The last inequality follows from concavity of sine on
\([0,\pi/2]\). Thus
\(R(\sin\theta+\cos\theta)<4025/4100<1\).
The real part of \(1-Re^{-i\theta}\) is positive and its imaginary
part is nonnegative. The displayed inequality says that its
imaginary part is smaller than its real part. Consequently
\[
                  A(y+t+ih)\le\pi/4\qquad(h\le0).
                                                                  \tag{11}
\]
The other two arguments in (8) have favorable signs. It follows that
\[
             \partial_h\Re Q\ge-\pi/4-2\pi a
                         \ge-\frac{15\pi}{8}\qquad(h\le0).
                                                                  \tag{12}
\]
Integration of (9) and (12) from the real axis gives
\[
 \Re Q(t+ih)-\Re Q(t)\le
 \begin{cases}
       (9\pi/5)h,&h\ge0,\\
       (15\pi/8)|h|,&h\le0 .
 \end{cases}                                                     \tag{13}
\]
All inequalities hold throughout (4), rather than only near a
critical point.

## 3. An exact real-integral identity

Orient the boundary of (4) counterclockwise. Let
\(\partial\mathcal R^+\) and \(\partial\mathcal R^-\) denote its
outer portions above and below the real axis, respectively, with
the induced orientations. They include the corresponding half
of each vertical side; neither includes a segment of the real axis.
The residue theorem gives
\[
 \begin{split}
 C_N^{\mathrm{mid}}(X,Y)
   &=N\int_{\ell_N}^{u_N}T_N(t;a,y)\,dt+\mathcal A_N(a,y),\\
 \mathcal A_N(a,y)
   &=\frac{N}{2i}\left\{
       \int_{\partial\mathcal R^+}
             T_N(s)[\cot(\pi Ns)+i]\,ds
       +\int_{\partial\mathcal R^-}
             T_N(s)[\cot(\pi Ns)-i]\,ds\right\}.
 \end{split}                                                     \tag{14}
\]
To check the coefficient and sign, begin with
\((2\pi i)^{-1}\int_{\partial\mathcal R}T_N\pi N\cot(\pi Ns)\,ds\).
Subtract the constant \(-i\) on the upper outer boundary and
\(+i\) on the lower one. Holomorphy gives integrals \(-I\) and
\(+I\) on those two boundaries, where
\(I=\int_{\ell_N}^{u_N}T_N(t)\,dt\). Their constant parts therefore
contribute \(NI\), exactly as in (14).

On a half-grid vertical side, the remainder kernels satisfy
\[
 \begin{cases}
 |\cot(\pi Ns)+i|\le2e^{-2\pi Nh},&h\ge0,\\
 |\cot(\pi Ns)-i|\le2e^{-2\pi N|h|},&h\le0 .
 \end{cases}                                                     \tag{15}
\]
Indeed \(e^{2\pi iN\ell_N}=e^{2\pi iNu_N}=-1\), so their
denominators have the form \(1+e^{-2\pi N|h|}\). There is no
pole at the real cut. On the two horizontal sides \(|h|=2\),
the corresponding bounds hold with the constant \(4\).

Combining (13) with (15) shows that the upper error integrand has,
relative to its real phase, the additional rate
\(-\pi h/5\). The lower error integrand has additional rate
\(-\pi|h|/8\). In particular the full vertical error is controlled
by the real values at its cut; there is no undecayed vertical
interval in (14).

## 4. Calibration to the actual next-source action

Keep the complete cap \(U_{0,N}(w,X)\), the ordinary-next reference,
and the affine action \(\Lambda_{123}\) of
[the selected-plateau comparison](research_mixed_next_filtered_selected_plateau.md).
The remaining variables and factors are
\[
 \begin{gathered}
 z=u+i\Im z_*,\quad u\in P,\quad Z=e^{-2\pi iz},\quad
                           \beta\in\{0,1\},\\
 d_N(Y)Y^{-N}C_{\beta,N}(Y,Z),\qquad |d_N(Z)|^{\beta/2}.
 \end{gathered}                                                   \tag{16}
\]
All subsequent estimates include both alternatives in the exact
Fourier-weight bound. No outgoing weight is inserted when \(\beta=0\).

Both real cut values in (14) have the strictly smaller disk profile
proved in the end-range theorem. At the selected radius
\(|Y|=e^{\pi/50}\), the continuous factorial numerator adds at most
\(t\pi/50\le\pi/50\). This is the same selected-radius allowance
used in the comparison theorem. Its continuous-index justification
is given in the end-range theorem: the maximal arc for
\(\log|1-Re^{i\theta}|\) is centered at \(\pi\), and for
length at most half a period its integral is at most
\(L(t)+t\log R\).

The full vertical remainders in (14) therefore have the same
calibrated gap as their real cut values, by (13)--(15).
Their lengths and the factor \(N\) change only a polynomial
prefactor. This controls both vertical sides all the way to
height \(2\), not just a short neighborhood of the real axis.

The horizontal remainders admit a separate uniform bound.
For every real \(t\in[\ell_N,u_N]\),
\[
 L(t)\le t\log2,\qquad I_a(t)\le t\log2,\qquad -J(t)<1/6.
\]
Consequently their real conditional profile satisfies
\[
       F_a(t)=L(t)+I_a(t)-3J(t)
                           <\log2+\frac12<\frac65.
                                                                  \tag{17}
\]
The complete cap has rate \(1549/1500\), and the selected-radius
allowance here is only \(t\pi/50\le\pi/100\).
At height \(2\), the smaller of the two alias losses is \(\pi/4\).
Thus the whole cap times either horizontal remainder has rate at most
\[
 \frac{1549}{1500}+\frac65+\frac{\pi}{100}-\frac{\pi}{4}
   =\frac{3349}{1500}-\frac{6\pi}{25}
   <\frac{2269}{1500}
   =\frac{77}{50}-\frac{41}{1500}.                              \tag{18}
\]
We used only \(\pi>3\). This is already below \(77/50\), before
allowing the larger selected-radius cost in the comparison theorem.
Finite factorial tolerances can be chosen strictly inside this
reserve and the reserves at the two cuts.

It follows that the error in (14), after multiplication by the
complete remaining source, obeys
\[
 \begin{split}
 &|U_{0,N}(w,X)\mathcal A_N(a,y)
           d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)|\,|d_N(Z)|^{\beta/2}\\
 &\hspace{15mm}\le C_\tau N^{B_\tau}
       \exp N\{\Lambda_{123}(z)-1/500+\tau\}.
 \end{split}                                                     \tag{19}
\]
The finite gap may be taken as \(1/1000\) after tolerances and
polynomial factors. The two omitted physical end ranges have
the same conclusion by the end-range theorem. In particular
replacing the whole conditional factor by the real main integral
in (14) incurs only this calibrated error on the selected
second-coordinate segment.

The statement is uniform for \(a\in[1/2,13/16]\), both next
types, all real ordinary colors, and both level parities.
The cap estimates hold on small complex neighborhoods of the
complete color. Fixed local outside-parameter derivatives follow
on smaller neighborhoods from the strict reserves and Cauchy's
formula, with conservative normalized gap \(1/2000\).
The row sets and real cuts are held fixed when taking these
derivatives; their dependence on \(a\) causes no derivative of a
moving summation range. The original outer integration factors
\(N\) are retained and cost only polynomial powers.

The remaining main term is still the actual oscillatory integral
\[
             N\int_{\ell_N}^{u_N}T_N(t;a,y)\,dt .                 \tag{20}
\]
Its contribution after the first-coordinate integration has not
been estimated here. Deforming (20) creates unweighted main-path
connectors, which must remain in that integral. The first-coordinate
vertical connector and the second-coordinate outer contour also
remain outside this theorem. No conclusion about the complete
\(343\) or \(344\) knot invariant follows from (19) alone.
