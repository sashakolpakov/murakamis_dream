# An angular gain for the complete transformed complementary contour

Research deduction, 7 November 2026. Retaining the outgoing angle
improves the uniform complementary-source ceiling on the actual
ordinary and attached type-four enclosures. The proof estimates
the entire original contour with every conditional row. It does
not assume a lower bound for the action selected by a following
tangle. No numerical evaluation is used.

## 1. Exact source and statement

Use the complete source, fixed contour and original normalization in
[the radial-majorant theorem](research_mixed_transformed_following_four_radial_majorant.md):
\[
\begin{split}
 f_{+,N}(w,Y)&=N\int_{\Gamma_+}U_{0,N}(w,e^{-2\pi ia})
                                  C_{1,N}(e^{-2\pi ia},Y)\,da,\\
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}
                 X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 \Gamma_+&:[1/2+ic,1/2]\cup[1/2,1],\qquad -7/200<c<0.
\end{split}                                                     \tag{1}
\]
The fixed incoming height is the already certified height of the
original ordinary pair. It does not change with the following
reference. The whole \(H_N\) coefficients stay inside \(U_0\).

Let \(O_4,A_4\) be the actual clipped output enclosures of
[the reference-domain theorem](research_mixed_actual_last_row_reference_domains.md).
Both lie in
\[
 \mathcal K=
 \left\{z=Z-is:
  |z-(3/10-13i/250)|\le3/50,\quad
  1/1000\le s\le27/250\right\}.
                                                               \tag{2}
\]
In particular
\[
 6/25\le Z\le9/25,\qquad
 R=e^{-2\pi s}>1/2,\qquad
 s\ge\frac{25}{3}(Z-3/10)^2-\frac1{125}.
                                                               \tag{3}
\]
The last inequality follows from
\(\sqrt{(3/50)^2-u^2}\le3/50-(25/3)u^2\), where
\(u=Z-3/10\). It preserves the actual disk correlation.

**Theorem 1.** For all sufficiently large integer \(N\), both
parities, and every fixed \(k,\ell\),
\[
 \sup_{\substack{w\in[-2,2]\\z\in O_4\cup A_4}}
 \left|\partial_w^k\partial_z^\ell
             f_{+,N}(w,e^{-2\pi iz})\right|
     \le C_{k,\ell}N^{B_{k,\ell}}
                           e^{(2281/1250)N}.            \tag{4}
\]
The value and fixed-derivative bound also hold on a fixed
neighborhood of these outgoing sets and on a sufficiently small
complex disk about \(w=-2\), after shrinking for derivatives.
The exponent in (4) has a strict analytic reserve before finite
products and parameter tolerances are paid.

More precisely, with \(D,B_0,H_0\) defined in (11), set
\[
\begin{split}
 \mathfrak C_{\rm ang}(Z-is)=\max\left\{\frac{793}{500},\
 B_0+H_0+\max_{0\le t\le1/3}
 \left[D(t)-\beta(e^{-2\pi s})t
  -\frac{4\pi^2}{9}t\left(Z-\frac{1-t}{2}\right)^2\right]\right\}.
\end{split}                                                     \tag{4a}
\]
For every \(\tau>0\), the same complete source and fixed
derivatives at \(z\in O_4\cup A_4\) obey the pointwise upper
rate \(\mathfrak C_{\rm ang}(z)+\tau\), uniformly on those sets.
This retains the outgoing angle, radius and row in one profile.
It may be combined with the previously proved radial ceiling by
taking the smaller bound for the same complete source.
Neither (4) nor (4a) is a normalized gap at every context-selected
critical point.

## 2. Uniform angular curvature of the numerator integral

Put
\[
 f_R(y)=\log|1-Re^{-2\pi iy}|,\quad
 I_{Z,R}(t)=\int_0^t f_R(Z+u)\,du,\quad
 \beta(R)=\frac12\log\frac2{1+R^2}.
                                                               \tag{5}
\]

**Lemma 2.** For \(1/2\le R\le1\) and
\(6/25\le y\le52/75\),
\[
                         f_R''(y)\le-\frac{8\pi^2}{9}.
                                                               \tag{6}
\]
Consequently, for \(6/25\le Z\le9/25\) and \(0\le t\le1/3\),
\[
 I_{Z,R}(t)
 \le L(t)-\beta(R)t
       -\frac{4\pi^2}{9}t\left[Z-\frac{1-t}{2}\right]^2,
 \qquad L(t)=-2J((1-t)/2).
                                                               \tag{7}
\]

*Proof.* Set \(q=\cos(2\pi y)\), \(A=1+R^2\).
On the stated interval \(q\le1/10\), since its largest cosine
is \(\cos(12\pi/25)=\sin(\pi/50)<1/10\).
Differentiating the regular logarithm gives
\[
 -\frac{f_R''(y)}{4\pi^2}
       =\frac{R(2R-Aq)}{(A-2Rq)^2}=k_R(q).
                                                               \tag{8}
\]
The sign of \(k_R'(q)\) is the sign of
\[
 6R^2-1-R^4-2R(1+R^2)q
 \ge6R^2-1-R^4-\frac{R+R^3}{5}.
                                                               \tag{9}
\]
The last polynomial equals \(5/16\) at \(R=1/2\);
its derivative is at least \(8R-4/5>0\) on \([1/2,1]\).
Thus \(k_R\) increases with \(q\). Its minimum is at \(q=-1\):
\[
                  k_R(q)\ge\frac{R}{(1+R)^2}\ge\frac29.
                                                               \tag{10}
\]
This proves (6).

At a fixed row length \(t\), the centered arc starts at
\(Z_0=(1-t)/2\), and its first derivative with respect to
the starting angle vanishes there. The interval between the
actual arc and that centered arc lies entirely in
\([6/25,52/75]\): their lowest endpoint is at least \(6/25\),
and their highest endpoint is at most \(9/25+1/3=52/75\).
The integrated second derivative is at most
\(-8\pi^2t/9\). The quadratic supporting inequality at \(Z_0\)
therefore gives the last term of (7). The centered radius
comparison (6)--(7) of the radial-majorant theorem gives its
first two terms. At \(t=0\) the statement is the exact zero
integral. \(\square\)

## 3. The whole lower-half source peaks before one third

Let
\[
 D(t)=L(t)-J(1/2-t)-3J(t),\quad
 B_0=1549/1500,\quad
 H_0=11/300+7/1920 .
                                                               \tag{11}
\]
The exact complete-cap bound on \(\Gamma_+\) is \(B_0\).
On its vertical part write \(a=1/2-i\delta/(2\pi)\),
where \(0\le\delta<11/50\). Before applying any outgoing
arc majorant, the actual conditional rate is
\[
 I_{Z,R}(t)-3J(t)+I_{1/2,e^{-\delta}}(t)+\delta t.
                                                               \tag{12}
\]
For \(1/3\le t\le1/2\), its derivative has exponential
\[
 \frac{|1-Re^{-2\pi i(Z+t)}|\,
          |1+e^{-\delta}e^{-2\pi it}|e^\delta}
      {(2\sin\pi t)^3}<\frac12.
                                                               \tag{13}
\]
Indeed the first modulus is at most two, the second at most one,
\(e^\delta<5/4\), and
\((2\sin\pi t)^3\ge3\sqrt3>5\).
This retains the original chirp. Thus (12) strictly decreases
on that interval. The same is true of the real far-half upper
profile
\[
                 I_{Z,R}(t)-3J(t)-J(1/2-t),
                                                               \tag{14}
\]
because its incoming logarithmic derivative is
\(\log(2\cos\pi t)\le0\), giving an even smaller bound.
Equation (14) is the original uniform incoming-angle majorant
on the real far half; the outgoing angle has not been maximized.

It therefore suffices to estimate \(0\le t\le1/3\) for every
lower-half row. On that interval the exact radial/chirp calculation
in the original complementary-contour proof gives
\[
 I_{1/2,e^{-\delta}}(t)+\delta t
          \le-J(1/2-t)+H_0.
                                                               \tag{15}
\]
Combining (7) and (11)--(15), all lower-half rows on the
entire path have rate at most
\[
 B_0+H_0+
 \max_{0\le t\le1/3}
 \left\{D(t)-\beta(e^{-2\pi s})t
   -\frac{4\pi^2}{9}t\left[Z-\frac{1-t}{2}\right]^2\right\}.
                                                               \tag{16}
\]
This is the retained correlated profile. It is a majorant for
the complete physical rows, not a replacement of \(U_0\) or
of a conditional row by a signed source at another target.

## 4. A strict uniform rational ceiling on the actual disk

The original scalar support is
\[
\begin{split}
 D(1/4)&<d_0=7/40-3/512+73/125,\\
 -1/10&<D'(1/4)<0,\qquad D''\le-2\pi\sqrt3<-10,\\
 C_{\rm base}&:=B_0+H_0+d_0+1/2000
                =350711/192000 .
\end{split}                                                     \tag{17}
\]
For the radius debit we will use
\[
 \beta(e^{-2\pi s})\ge
                 \min\{(5/2)s,1/20\}\qquad(s\ge0).
                                                               \tag{18}
\]
To prove it for \(0<s\le1/50\), use
\[
 \beta(e^{-2\pi s})=\pi s-\tfrac12\log\cosh(2\pi s)
                 \ge\pi s-\pi^2s^2>(5/2)s.
                                                               \tag{19}
\]
Here \(\log\cosh u\le u^2/2\) follows by integrating
\(\tanh u\le u\); also \(\pi s<1/10\) and \(\pi>3\).
For \(s\ge1/50\), monotonicity of \(\beta\) gives
\(\beta\ge1/20\). Its value at zero is zero.

For \(t\le1/5\), the quadratic support in (17) gives
\[
                  D(t)<d_0-3/400 .
                                                               \tag{20}
\]
Consequently (16) is at most \(C_{\rm base}-1/125\) there.
For the rest of the proof suppose \(1/5\le t\le1/3\).
If \(s\ge1/50\), the radius debit is at least \(1/100\),
already more than the required loss below \(C_{\rm base}\).
It remains to consider \(1/1000\le s\le1/50\).

Put \(d=3/8-Z>0\), \(u=Z-3/10\).
First let \(1/5\le t\le1/4\). By \(\pi>3\), the
radius and angular losses in (16) are at least
\[
                        \frac{s}{2}+\frac45d^2.
                                                               \tag{21}
\]
If \(Z\le1/3\), then \(s\ge1/1000\), \(d\ge1/24\),
so (21) is at least
\[
                    \frac1{2000}+\frac1{720}
                              =\frac{17}{9000}.
                                                               \tag{22}
\]
If \(Z\ge1/3\), the disk correlation (3) instead gives
\[
 \frac{s}{2}+\frac45d^2
 \ge \frac{149}{30}u^2-\frac3{25}u+\frac1{2000}.
                                                               \tag{23}
\]
This quadratic increases for \(u\ge1/30\); its derivative
there is at least \(19/90\). Its value at \(1/30\) is
\(109/54000>17/9000\). Thus (22) holds throughout this
middle row interval.

Finally take \(1/4\le t\le1/3\), and write \(r=t-1/4\).
The signed derivative in (17), rather than its absolute bound,
gives \(D(t)<d_0-5r^2\).
The total radius, angle and quadratic losses relative to \(d_0\)
are therefore at least
\[
 \frac58s+5r^2+(d-r/2)^2
       \ge\frac58s+\frac{20}{21}d^2.
                                                               \tag{24}
\]
If \(Z\le1/3\), this exceeds \(1/500\), since it is at
least \(1/1600+5/3024>1/500\).
If \(Z\ge1/3\), (3) gives the lower bound
\[
 \frac{345}{56}u^2-\frac17u+\frac1{2800}.
                                                               \tag{25}
\]
Its derivative is positive for \(u\ge1/30\); its minimum
there is \(41/16800>1/500\).

These three row intervals prove that the rate (16) is strictly
below \(2281/1250\), uniformly on \(\mathcal K\).
For the tight middle interval the explicit remaining reserve is
\[
 \frac{2281}{1250}-
       \left(C_{\rm base}-\frac{17}{9000}\right)
                         =\frac{199}{2880000}>0 .
                                                               \tag{26}
\]
The low interval has the larger loss \(1/125\).
For the final interval use
\(B_0+H_0+d_0=C_{\rm base}-1/2000\);
the loss \(1/500\) in (24) is again sufficient.
If \(s\ge1/50\), its loss \(1/100\) is larger still.

## 5. All remaining rows, finite products and derivatives

The original upper-half estimate on the complete connector and
real far half has rate at most \(793/500<2281/1250\).
It holds on the whole outgoing unit disk, so it covers every
row \(j/N\ge1/2\) here, including the even half row and the true
last physical row. The \(j=0\) row is already included by the
continuous lower rate at zero. No support zero is replaced by
off-grid termination.

Use the same zero-safe numerator-product upper estimates and
the same uniform denominator \(O(\log N)\) estimates as in
the radial-majorant theorem. They apply before summing the full
coherent cap and all \(N\) conditional rows.
Allocate their tolerances from the positive reserve (26).
The path length and the original factor \(N\) cost only a
polynomial factor. This proves (4) for values.

The incoming cap has the existing uniform all-real-color bound;
its fixed ordinary derivatives follow by applying Markov's
inequality to complete coefficient polynomials before the positive
sum. The outgoing set is compact and has radii strictly between
zero and one. Its rate integrals and finite-product upper bounds
are continuous uniformly on a fixed neighborhood. A sufficiently
small enlargement of that set spends only a prescribed fraction
of (26), even if its points no longer satisfy the exact disk
constraint (3). Cauchy's formula on smaller neighborhoods gives
all fixed outgoing derivatives. The same tolerance argument
using the original cap's complex-color bounds gives a fixed disk
near \(w=-2\). All source estimates preserve both parities.

The angular estimate does not change the original selected
action or its additive constant. At a following reference one
must still compare its pre-Gram prefix action to this complete
source ceiling, or to the smaller of (16) and the radial bound.
The full first path and both later Fourier sectors remain
separate parts of that observation. The theorem proves a stronger
complete complementary-source estimate on the required domains,
without promoting it to an unproved following-family gap.
