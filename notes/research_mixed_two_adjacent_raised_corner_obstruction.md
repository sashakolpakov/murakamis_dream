# A competing raised corner in the complete merged pair

Research deduction, 7 November 2026. On the full principal raised
rectangle for the original two-Fourier-end power-two pair, the
zero-extended upper-right corner has strictly larger real phase
than the proved central critical point. The difference is bounded
below by an explicit positive rational constant. Thus an absolute
bound on this whole raised rectangle cannot justify the central
Gaussian. The signed finite pair and its complete contour identity
remain unchanged.

This is an analytic comparison, using only the original branch
formulas and elementary rational series bounds. No numerical
evaluation, source replay, or optimization is used.

## 1. The original upper phase on the full rectangle

Use the exact merged row and original phase from
[the complete source](research_mixed_two_adjacent_merged_source.md),
equations (16), (21)--(22):
\[
\begin{split}
 \mathscr R_N(a,s;x,y)
 &=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(a+x)\Pi_N(s+y)
                 E_N(a)^2E_N(s)^2E_N(x)E_N(y),\\
 F(a,s;x,y)
 &=g(a+s)+g(a+x)+g(s+y)-2g(a)-2g(s)\\
 &\hspace{20mm}-g(x)-g(y)+2\pi ias.
\end{split}
 \tag{1}
\]
Set \(x=y=x_0=\xi+i\upsilon\), and let
\(a_*=\alpha+ih\) be the actual symmetric critical index from
[the critical-corridor theorem](research_mixed_two_adjacent_critical_corridor.md).
Both internal contours have height \(h>1/20\). Every argument
in (1) therefore has positive height on the entire raised
rectangle, including the zero-extended region \(\Re(a+s)>1\).
Use the actual global upper primitive \(g_+\), not a periodic
version of the regular-strip primitive.

For \(0<R<1\), define the absolutely convergent real series
\[
 D_R(t)=-\frac1{2\pi}\sum_{n\ge1}
                         \frac{R^n\sin(2\pi nt)}{n^2}.
 \tag{2}
\]
The original upper/lower reflection formula is exactly
\[
 \Re g_+(t+iH)=D_{e^{-2\pi H}}(t)+\pi H(2t-1),
                                      \qquad H>0.
 \tag{3}
\]
This follows from the lower dilogarithm formula and its
original quadratic chirp; see
[the global phase calculation](research_mixed_complex_horizontal_obstruction.md),
equations (6)--(7).

Put
\[
                  r=e^{-2\pi h},\qquad
                  \rho=e^{-2\pi\upsilon},\qquad \tau=r\rho.
 \tag{4}
\]
For real coordinates \(p,q\), substitution in (1) gives
\[
\begin{split}
 R(p,q):={}&\Re F(p+ih,q+ih;x_0,x_0)\\
 ={}&D_{r^2}(p+q)+D_\tau(p+\xi)+D_\tau(q+\xi)
           -2D_r(p)-2D_r(q)-2D_\rho(\xi)\\
    &+2\pi\upsilon(p+q)+4\pi h\xi .
\end{split}
 \tag{5}
\]
In particular the rate is not periodic. The exact original
phase law is
\[
 F(a+1,s)=F(a,s)-2\pi ix_0,\qquad
 F(a,s+1)=F(a,s)-2\pi ix_0,
 \tag{6}
\]
so either positive real period shift gains \(2\pi\upsilon\)
in real part.

Write \(M=R(\alpha,\alpha)\) for the central rate, without
the common external chirp. The limiting raised corner obeys
\[
\begin{split}
 \Delta:=R(1,1)-M
 ={}&4\pi\upsilon(1-\alpha)+2D_\tau(\xi)
       -D_{r^2}(2\alpha)-2D_\tau(\alpha+\xi)+4D_r(\alpha).
\end{split}
 \tag{7}
\]

## 2. Exact bounds inherited from the critical point

Let
\[
 T=\cot(\pi a_*)=u-iv,\qquad Z=e^{2\pi ia_*}=r e^{i\theta},
                     \quad \theta=2\pi\alpha.
 \tag{8}
\]
The critical-corridor proof established
\[
 \frac15<v<\frac14,\qquad
        \frac{127}{364}<u<\frac{13}{31},\qquad
                         \frac13<\alpha<\frac5{12}.
 \tag{9}
\]
A small refinement of the same inverse-cotangent calculation is
\[
                              \alpha<\frac25.
 \tag{10}
\]
Indeed its angle \(B=\pi-2\pi\alpha\) satisfies
\(0<B<\pi/2\) and \(\tan B>3/4\). Also
\(\tan^2(\pi/5)=5-2\sqrt5<9/16\), since
\(\sqrt5>71/32\). Thus \(B>\pi/5\), proving (10).

Write \(Z=-A+iB_1\), with \(A,B_1>0\). The exact formulas
\[
 A=\frac{1-u^2-v^2}{u^2+(1+v)^2},\qquad
 B_1=\frac{2u}{u^2+(1+v)^2},\qquad
 r^2=\frac{u^2+(1-v)^2}{u^2+(1+v)^2}
 \tag{11}
\]
give the convenient bounds
\[
        r<\frac57,\qquad A<\frac{27}{50},\qquad
                       \frac25<B_1<\frac{13}{25}.
 \tag{12}
\]
Here are exact witnesses. The last ratio in (11) increases
with \(u\) and decreases with \(v\) in the relevant rectangle.
Using \(u<3/7,\ v>1/5\),
\[
                     r^2<\frac{1009}{1989}<\frac{25}{49}.
 \tag{13}
\]
Further, \(87/250<u<21/50\). Thus
\[
 A<\frac{52431}{97569}<\frac{27}{50}.
 \tag{14}
\]
For the upper bound on \(B_1\), its dependence on \(u\)
is increasing for \(u<1+v\), and it decreases with \(v\);
hence
\[
                    B_1<\frac{2100}{4041}<\frac{13}{25}.
 \tag{15}
\]
For the lower bound, bound the numerator below and denominator
above separately:
\[
                    B_1>\frac{6960}{17389}>\frac25 .
 \tag{16}
\]
All comparisons are rational.

For the original external endpoint, put \(\phi=2\pi\xi\).
The inherited analytic bounds are
\[
 \rho<\frac{123}{200},\quad
 \cos\phi>\frac25,\quad \sin\phi<\frac{23}{25},\quad
 \upsilon>\frac{157}{2000},\quad \pi>\frac{157}{50}.
 \tag{17}
\]
The radius and cosine bounds are proved in
[allocation curvature](research_mixed_fourier_allocation_curvature.md),
equation (6). The sine bound is in
[the right-critical-sheet proof](research_mixed_three_fourier_conditional_right_critical_sheet.md),
equation (7). The height and \(\pi\) bounds are the same
original rational parameter bounds used there. In particular
\[
                            \tau<\frac{123}{280}.
 \tag{18}
\]

## 3. A positive corner-minus-critical gap

Multiply (7) by \(2\pi\). The even internal powers cancel
exactly, giving
\[
\begin{split}
 2\pi\Delta
 ={}&8\pi^2\upsilon(1-\alpha)
       -4\sum_{\substack{n\ge1\\n\ {\rm odd}}}
                       \frac{r^n\sin(n\theta)}{n^2}\\
    &+2\sum_{n\ge1}
       \frac{\tau^n[\sin n(\theta+\phi)-\sin(n\phi)]}{n^2}.
\end{split}
 \tag{19}
\]
Absolute convergence justifies this regrouping. The cancellation
is the exact identity
\(4\operatorname{Li}_2(z)-\operatorname{Li}_2(z^2)
 =4\sum_{n\ {\rm odd}}z^n/n^2\).

The positive linear term has the lower bound
\[
 8\pi^2\upsilon(1-\alpha)
    >\frac{24}{5}\left(\frac{157}{50}\right)^2
                       \frac{157}{2000}
     =\frac{92877432}{25000000}>\frac{37}{10}.
 \tag{20}
\]
We bound the possible losses in the two sums separately.

The first internal term loses less than
\[
                           4r\sin\theta=4B_1<\frac{52}{25}.
 \tag{21}
\]
The rest of the odd sum loses at most
\[
 \frac{4r^3}{9}+\frac{4r^5}{25(1-r^2)}
      <\frac{500}{3087}+\frac{125}{2058}
       =\frac{1375}{6174}<\frac9{40}.
 \tag{22}
\]

The first output term is exactly
\[
 2\rho\{B_1\cos\phi-(A+r)\sin\phi\}.
\]
By (12), (17), its possible loss is less than
\[
 \frac{123}{100}
       \left\{\left(\frac{27}{50}+\frac57\right)
                         \frac{23}{25}-\frac4{25}\right\}
       =\frac{1069731}{875000}<\frac{49}{40}.
 \tag{23}
\]
For the second term, \(\alpha+\xi\in(1/2,3/4)\), by
(9)--(10) and \(1/6<\xi<1/4\). Therefore
\(\sin 2(\theta+\phi)>0\), and its loss is at most
\(\tau^2/2\). All terms starting at three lose at most
\(4\tau^3/[9(1-\tau)]\). Thus their total is less than
\[
 \frac12\left(\frac{123}{280}\right)^2
  +\frac{4(123/280)^3}{9(1-123/280)}
  =\frac{36264213}{221558400}<\frac16.
 \tag{24}
\]
These bounds use signed second-order information before bounding
the remaining tail. No sine or dilogarithm was evaluated.

Combining (20)--(24) proves
\[
 2\pi\Delta>
 \frac{37}{10}
    -\left(\frac{52}{25}+\frac{49}{40}
                         +\frac9{40}+\frac16\right)
 =\frac1{300}.
 \tag{25}
\]
Consequently
\[
 \boxed{\quad
 R(1,1)-R(\alpha,\alpha)>
                  \frac1{600\pi}>\frac7{13200}>0 .
 \quad}
 \tag{26}
\]

## 4. Consequence for the actual principal rectangle

The exact merged-source contour uses
\[
 \alpha_N=-1/(3N),\qquad\beta_N=1-1/(3N)
 \tag{27}
\]
in each variable. The corner \((1,1)\) in (26) is a limiting
real coordinate, not an added physical node. Continuity of
the original positive-height phase implies that a fixed small
square with real coordinates strictly less than one and
strictly greater than \(1/2\) has
\[
                     R(p,q)>M+\delta
 \tag{28}
\]
for some fixed \(\delta>0\). This square is contained in
\([\alpha_N,\beta_N]^2\) for all sufficiently large \(N\).
It is wholly in the zero-extended triangle \(p+q>1\).

The global upper-half-plane factorial packet applies uniformly
on this fixed square. Its arguments have positive heights,
so no factorial zero or real-axis singularity occurs there.
The leading coefficient is nonzero. Thus the exact raised
row has a matching lower modulus bound on this square, with
its original polynomial power \(N^{-3/2}\).
In particular the absolute integral of the full principal
rectangle cannot be bounded by a polynomial times \(e^{NM}\).
Including the common outside factor \(e^{\pi iD(x_0+x_0)}\)
changes both rates by the same amount and does not remove
the gap (26).

The physical added rows in this region vanish through
\(\Pi_N((j+k)/N)=0\). Their positive-height interpolation
does not vanish and cannot be removed termwise. The complete
finite contour identity still retains its endpoint currents,
period factors, and Fourier corrections. Those terms, or a
different coherent organization of the same source, are needed
to control this raised region.

No lower bound for the signed principal integral is asserted.
The comparison does not disprove a central packet for the
complete pair: oscillation within the main integral or its
cancellation with the other exact currents may change its
exponential behavior. It disproves precisely the proposed
global absolute dominance of the selected central saddle
on the whole raised rectangle.

