# Two checks on earlier adjacent-pair contour choices

The successful full-period rectangle avoids the diagonal staircase of the triangular index domain. This note preserves two useful calculations from the preceding contour search: an elementary bound for a principal deformation, and an explicit obstruction to separately estimating deep staircase corners. Neither calculation is a substitute for the exact grouped rectangle identity.

Use the phase \(W\), heights \(h_x,h_y,h_a\), and selected rate \(M\) from [the grouped contour bounds](research_adjacent_pair_grouped_contour_bounds.md).

## 1. A bounded principal deformation

Keep \(x=a+ih_x\) and move \(y=b+ik\) from height \(h_a\) to height \(h_y\) over the triangle \(0\le b\le1/2\), \(0\le a\le1-b\). The \(a=0\) boundary ribbon has zero pullback of \(dx\wedge dy\), since \(x\) is constant there. The other three ribbons have strict rate bounds.

Set \(R=1/\sqrt8\), \(r=e^{-2\pi k}\), \(X=Re^{2\pi ia}\), \(Y=re^{2\pi ib}\). Then
\[
\begin{split}
 \Re W={}&\pi k+\pi a(-4h_x+2k)+2\pi b(h_x-k)\\
 &+\frac1{2\pi}\Im\{3\operatorname{Li}_2(X)+6\operatorname{Li}_2(Y)
       -\operatorname{Li}_2(XY)-\operatorname{Li}_2(Y^2)\}.       \tag{1}
\end{split}
\]
The bound \(|\operatorname{Li}_2(z)|\le |z|+|z|^2/[4(1-|z|)]\) gives
\[
 3D(R)+D(Rr)<3(81/200)+13/48=1783/1200.
\]
Indeed \(R<71/200\), \(R^2=1/8\), \(R<3/8\), and \(Rr\le1/4\).

At \(b=0\), the two \(Y\)-dilogarithms are real and the coefficient of \(a\) is negative. Thus the bottom rate is less than
\[
 \frac12+\frac{1783}{7200}<\frac34.
\]
At \(b=1/2\), the constant polynomial term is \(\pi h_x\). Using \(\log2<7/10\), \(\pi>157/50\), the top rate is less than
\[
 \frac{21}{40}+\frac{1783}{1200}\frac{25}{157}
       =\frac{28697}{37680}<\frac{61}{80}.
\]
On \(a=1-b\), the polynomial term is at most
\[
 \pi(k-h_x)\le\frac14\log(7/8)<-1/32.
\]
Also \(\Im\operatorname{Li}_2(X)\le0\), and \(XY\) is positive real. Split the remaining series into odd and even terms:
\[
 6\operatorname{Li}_2(Y)-\operatorname{Li}_2(Y^2)
 =6\sum_{m\ {\rm odd}}\frac{Y^m}{m^2}
  +2\sum_{m\ {\rm even}}\frac{Y^m}{m^2}.
\]
At \(r\le1/\sqrt2\), the absolute odd sum is at most
\(6r+6r^3/9+6r^5/[25(1-r^2)]=(484/75)r\);
the even sum is at most \(5/16\). The diagonal rate is therefore less than
\[
 \left(\frac{484}{75}\frac{71}{100}+\frac5{16}\right)
 \frac{25}{157}-\frac1{32}
 =\frac{281887}{376800}<\frac34.
\]
All three bounds are below \(M>23/30\). These bounds concern the ordinary principal holomorphic integral; they do not bound a separate lattice endpoint current.

## 2. A deep triangular corner that cannot be estimated separately

Put \(y=1/4\), \(x=a-iH\), \(H\ge1\), with \(a\) near \(3/4\) on the original side of the triangular boundary. For \(w=e^{-2\pi ix}\), \(Y=i\), the lower-half-plane formula for \(J\) gives the exact identity
\[
 W(x,y)-2\pi ix
 =V(y)+\frac{i}{2\pi}
       \{3\operatorname{Li}_2(w)-\operatorname{Li}_2(w/Y)\},
\]
where \(V(y)=-6J(y)+J(2y)+i\pi y^2-i\pi/6\). At \(y=1/4\),
\[
 \Re V(1/4)=3G/\pi>189/220,\qquad
 G=\sum_{m\ge0}(-1)^m/(2m+1)^2.
\]
This follows from \(G>1-1/9+1/25-1/49>9/10\) and \(\pi<22/7\).

The positive exponential series through degree thirteen proves \(e^6>400\); hence \(|w|<1/400\). The dilogarithm term above has modulus less than \(2/1197\). Thus
\[
 \Re W(a-iH,1/4)-2\pi H
 >189/220-2/1197>17/20>M.
\]
The upper bound for \(M\) follows from the certified local inequality
\[
 M\le F(p)+|\nabla F(p)|^2/4<17/20,\qquad p=(31/400,1/4),
\]
where \(F\) is the real phase on the selected upper surface and
\(-\nabla^2F\ge2I\) on its local rectangle.

This defeats a separate exponential bound for every deep diagonal corner of the triangular cell decomposition. It does not defeat their cancellation. The full-period zero extension removes the staircase and permits the exact grouping used in the final contour argument.

## 3. Reproduction

The following script checks all displayed fraction comparisons and the certified upper bound for \(M\):

~~~sh
python3 experiments/verify_adjacent_pair_connector_bounds.py --output repro/results/research-adjacent-pair-connector-bounds.json
~~~

It imports the existing rational horizontal enclosures; no floating-point optimizer is used. The [saved results](../repro/results/research-adjacent-pair-connector-bounds.json) are separate from the successful grouped-contour certificate.
