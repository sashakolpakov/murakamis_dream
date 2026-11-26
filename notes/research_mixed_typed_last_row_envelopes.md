# Two typed envelopes for ordinary last-row references

Research deduction, 5 November 2026. Two convex typed domains contain
all four ordinary/attached external-leg domains from the
[actual-reference reduction](research_mixed_actual_last_row_reference_domains.md).
They reduce its twenty sufficient own/type/role products to six
own/type products, with both conditional orientations retained.
This simplifies the required domains; it proves no last-row sign.

## 1. The two enclosures

Keep the reduced disks
\[
 P_3=\{|z-(7/20-i/100)|\le83/1000\},\qquad
 P_4=\{|z-(3/10-13i/250)|\le3/50\}.
 \tag{1}
\]
Writing \(z=x+ih\), define
\[
 \begin{split}
 K_3&=P_3\cap
  \{-9/125\le h\le17/250,\quad x-3h\le76/125\},\\
 K_4&=P_4\cap\{-27/250\le h\le-1/1000\}.
 \end{split}
 \tag{2}
\]
Let \(O_3,O_4,A_3,A_4\) be exactly the closed domains
in equations (1)--(2) of the actual-reference reduction.

**Proposition 1.**
\[
                     O_3\cup A_3\subset K_3,\qquad
                     O_4\cup A_4=K_4.
 \tag{3}
\]
All domains in (2) are compact and convex, have nonempty interior,
and remain in the previously admitted reduced disks. The actual
ordinary and attached legs lie in their interiors. The first
inclusion is a sufficient enlargement; neither equality there nor
minimality as a convex hull is asserted.

For type four, the forward inclusion in (3) follows directly from
the height ranges of \(O_4,A_4\). Conversely take \(x+ih\in K_4\).
If \(h\ge-51/500\), it belongs to \(O_4\).
For the remaining strip \(-27/250\le h\le-51/500\),
the disk equation gives
\[
 |x-3/10|^2
 \le(3/50)^2-(h+13/250)^2
 \le\frac{11}{10000}<\frac1{400}.
 \tag{4}
\]
Indeed \(|h+13/250|\ge1/20\) on this strip.
Thus \(1/4<x<7/20\), which is contained in the attached
real range \([123/500,7/20]\). Its height is also in the
attached range \([-27/250,-1/50]\), so it belongs to \(A_4\).
This includes both strip endpoints; the common height
\(-51/500\) may be assigned to either set.

For type three, the height ranges of \(O_3\) and \(A_3\)
already lie in (2). On the ordinary strip
\(-13/200\le h\le17/250\), the right edge of the disk is
\[
 x_+(h)=\frac7{20}
       +\sqrt{(83/1000)^2-(h+1/100)^2}.
 \tag{5}
\]
The square root is strictly positive throughout this closed strip.
Its derivative
\(-(h+1/100)/\sqrt{(83/1000)^2-(h+1/100)^2}\)
decreases as \(h\) increases. Therefore
\[
 x_+'(h)\le\frac{55}{2\sqrt{966}}<1<3,
 \qquad
 \max_h\{x_+(h)-3h\}
       =\frac{109}{200}+\frac{\sqrt{966}}{500}
       <\frac{76}{125}.
 \tag{6}
\]
The two strict rational comparisons are
\(55^2=3025<4\cdot966=3864\) and
\(4\cdot966=3864<63^2=3969\).
Every other point at the same height has \(x\le x_+(h)\),
so the slanted inequality holds on all of \(O_3\).
For the attached rectangle, directly
\[
                x-3h\le\frac{391}{1000}
                              +3\frac9{125}
                         =\frac{607}{1000}
                         <\frac{76}{125}.
 \tag{7}
\]
Intersecting with the disk preserves this inequality.
This proves (3).

The two disk centers satisfy every clipping inequality strictly,
so both \(K_3,K_4\) have nonempty interior. Actual legs have
the strict disk and ordinary/attached bounds already proved in
the cited reduction. Equations (6)--(7) give additional strict
room at the slanted side. Hence they lie in the interiors of the
new domains as stated.

## 2. The complete boundaries

The boundary of \(K_4\) consists of the admitted portions of its
circle and its two horizontal clipping chords. The boundary of
\(K_3\) consists of its admitted circle portions, its two
horizontal chord segments, and the slanted chord
\(x-3h=76/125\). Each piece is clipped by all the remaining
inequalities; no full untrimmed chord is silently substituted.

For an explicit check that the new slanted segment has no missing
endpoint, its lower endpoint is
\((x,h)=(49/125,-9/125)\), strictly inside \(P_3\).
Its upper endpoint lies on the circle at
\[
 h_*=-\frac{49}{625}+\frac{\sqrt{16906}}{10000},\qquad
 x_*=\frac{233}{625}+\frac{3\sqrt{16906}}{10000}.
 \tag{8}
\]
Here \(-9/125<h_*<-13/200\), since
\(64^2<16906<134^2\). The other intersection of this line
with the circle uses the negative square root and has height less
than \(-49/625<-9/125\), outside the clipped domain.
At the lower endpoint, the squared distance to the disk center is
\(5608/10^6<6889/10^6\); thus the horizontal/slanted
intersection is indeed present. The upper horizontal chord has
no additional slanted cut, since its line threshold is
\(76/125+3(17/250)=203/250\), greater than the disk's
rightmost real coordinate \(433/1000\).
All remaining endpoints are the corresponding circle/line
intersections. Closed endpoints and repeated descriptions of a
corner may be retained.

## 3. Six sufficient products with the original reference map

An ordinary factor at vertex \(j\), \(2\le j\le m-1\),
has external legs \(t_{j-1}\) and \(s_{j+1}\). By (3),
each belongs to \(K_n\) of its own neighboring type,
regardless of whether its role is ordinary or attached.
This includes the two-attached case \(m=3,j=2\). The private
legs \(s_1,t_m\) are still not external inputs of this ordinary
map, and no ordinary factor of this form occurs at \(m=1,2\).

For each own flag \(\epsilon\in\{0,1\}\), it therefore
suffices to use the three products
\[
                  K_3\times K_3,\qquad
                  K_3\times K_4,\qquad
                  K_4\times K_4,
 \tag{9}
\]
and retain both original conditional orientations. Exchanging
the two external inputs exchanges the two original roots and
the orientations. Thus (9) covers both ordered mixed-type cases.
There are six own/type families in total. Some points of these
independent products need not be realized by any open word.
In particular replacing the role-specific type-three domains
by \(K_3\) asks for a potentially stronger sufficient inequality.

Let \(D\) denote the exact complete revived-row deficit from
equation (5) of the actual-reference reduction, with its original
root correlation, first and second allocated halfweights,
four carrier branches and unchanged supporting plane. For any
product \(K\) in (9), its same boundary principle gives
\[
 \max_{K\times I^2}D
 \le\max\left\{-\frac1{1000},
                  \max_{\partial K\times I^2}D\right\},
 \qquad I=[11/50,9/20].
 \tag{10}
\]
Indeed the original branch is holomorphic on a neighborhood of
the reduced product and hence of \(K\). Its retained-variable
map is locally open, its negative horizontal Hessian exceeds
twice the prescribed quadratic coefficient, and its matched
full-row gap remains \(1/1000\). At an interior maximizing
reference the same cancellation forces the target real parts
to equal the reference real parts, contradicting a larger value.
Compactness supplies the maximum; differentiability of a
maximizing carrier branch or target is not needed.

The boundary in (10) is
\((\partial K_L\times K_R)\cup(K_L\times\partial K_R)\).
It retains the full two-dimensional interior of the other input,
as well as every horizontal and slanted boundary segment just
described. Checking only two-circle distinguished boundaries
would not establish (10)'s required boundary inequality.

This deduction neither evaluates that inequality nor changes
the source/geometry theorems. In particular it supplies no
last-row sign, no new root enclosure, and no assertion for the
different terminal endpoint graphs.
