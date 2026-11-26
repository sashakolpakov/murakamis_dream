# A uniform quadratic credit from the own-four neighbor height

Research corollary, 7 November 2026. The ordinary-index restriction
\(.22\le v\le.4\) makes the favorable two-incidence height
derivative uniform over the neighbor's entire real interval.
The resulting credit is \((2\pi/3)\lambda_b^2(x-.1)\).
It requires no new source evaluation or reference enclosure.

Keep every actual source restriction and notation of
[the neighbor-height theorem](research_mixed_first_attached_neighbor_height_credit.md).
In particular \(b=z+ih\), \(.1\le z\le.5\),
\(-.108\le h\le0\), the first ordinary index is real with
\(.22\le v\le.4\), and the following regular index is
\(t=w+i\zeta\), where
\[
                   .22\le w\le.49,\qquad -.108\le\zeta\le.068 .
 \tag{1}
\]
The following source estimate must independently be valid.
The first index interval is justified by the newly proved
[upper barrier](research_mixed_first_attached_four_upper_index_barrier.md);
it is essential to the bound below.

The exact original two-incidence force is
\[
 B(v,t;z,h)=
 \Im\{g'(v+z+ih)+g'(t+z+ih)-3g'(z+ih)+2\pi it\}.
 \tag{2}
\]

**Proposition 1.** Throughout this domain,
\[
                            \partial_h B<-2\pi/3.             \tag{3}
\]
Consequently, on the actual active first-minimum path
\(h=-\lambda_b d\), \(d=x-.1\), \(0\le\lambda_b\le17/20\),
\[
 \boxed{\quad
 \lambda_b B(v,t;z,-\lambda_b d)
 \ge \lambda_b B(v,t;z,0)+\frac{2\pi}{3}\lambda_b^2d .
 \quad}                                                       \tag{4}
\]
Equality is allowed when \(d=0\) or \(\lambda_b=0\).

*Proof.* The original derivative identity is
\[
 \frac{\partial_h B}{\pi}=
 \Re\cot\pi(v+z+ih)+
 \Re\cot\pi(w+z+i(h+\zeta))-3\Re\cot\pi(z+ih).
 \tag{5}
\]
We use only \(\cosh(2\pi h)<5/4\), the exact cotangent
formula and elementary trigonometric bounds already proved
in the neighbor-height theorem.

For \(.1\le z\le.15\),
\(\sin(2\pi z)>29/50\) and
\(\cos(2\pi z)>29/50\), so
\(\Re\cot\pi(z+ih)>58/67\).
Each shifted real cotangent in (5) is less than \(2/3\).
It follows that
\[
             -\partial_h B/\pi>174/67-4/3=254/201>2/3 .
 \tag{6}
\]
For \(.15\le z\le.2\), instead use
\(\sin(2\pi z)>4/5\), \(\cos(2\pi z)>3/10\).
Thus the unshifted real cotangent is greater than \(16/19\).
Both shifted real arguments are now at least \(.37\);
their real cotangents are less than \(1/2\).
Hence
\[
                        -\partial_h B/\pi>48/19-1=29/19>2/3 .
 \tag{7}
\]
For \(.2\le z\le.28\), the already proved bound
\(-\partial_h B/\pi>104/87\) suffices.
These estimates are uniform in the following height \(\zeta\).

It remains to consider \(.28\le z\le.5\).
The following shifted argument \(w+z\) is at least \(1/2\)
and less than one, so its real cotangent in (5) is
nonpositive. Set
\[
 C=5/4,\qquad f_C(y)=\frac{\sin(2\pi y)}{C-\cos(2\pi y)} .
 \tag{8}
\]
The unshifted sine is nonnegative and the first shifted
sine is nonpositive. Increasing their common hyperbolic
denominator parameter to \(C\) therefore gives
\[
 -\partial_h B/\pi
 \ge 3\Re\cot\pi(z+ih)-\Re\cot\pi(v+z+ih)
 \ge 3f_C(z)-f_C(z+v).                                      \tag{9}
\]

For \(r\in[-1,1]\), put
\[
             k(r)=\frac{1-Cr}{(C-r)^2}.
 \tag{10}
\]
Then \(f_C'(y)=-2\pi k(\cos2\pi y)\).
On \(r\in[-1,0]\), \(k(r)\ge k(-1)=4/9\).
On the entire interval \([-1,1]\), \(k(r)\le25/36\):
indeed
\[
 k'(r)=\frac{2-C^2-Cr}{(C-r)^3},
 \tag{11}
\]
whose only zero is \(r=7/20\), a maximum with value
\(25/36\).
Since \(\cos2\pi z\le0\) on the present \(z\) interval,
\[
 \frac{d}{dz}\{3f_C(z)-f_C(z+v)\}
 \le 2\pi\left(-\frac43+\frac{25}{36}\right)
                         =-\frac{23\pi}{18}<0.              \tag{12}
\]
Its minimum in \(z\) is consequently at \(z=.5\).

At that endpoint, the last expression in (9) becomes
\[
                 \frac{\sin(2\pi v)}{C+\cos(2\pi v)}.
 \tag{13}
\]
Its derivative has the sign of \(1+C\cos(2\pi v)\),
which decreases strictly as \(v\) runs from \(.22\)
to \(.4\). Thus its minimum is at a \(v\) endpoint.
At \(v=.22\),
\[
 \sin(.44\pi)=\cos(.06\pi)>49/50,\qquad
 \cos(.44\pi)=\sin(.06\pi)<1/5,
 \tag{14}
\]
so (13) exceeds \(98/145>2/3\).
At \(v=.4\), use
\(\sin(.8\pi)>29/50\) and
\(\cos(.8\pi)<-4/5\); the ratio exceeds \(58/45>2/3\).
Equations (9)--(14) prove (3) on the remaining interval.
Integration at the actual correlated height proves (4).
\(\square\)

The larger local credits in the neighbor-height theorem
may still be retained wherever they are stronger than (4).
The first-index height reduction and its separate
\(47\pi(-\eta)/2009\) credit are unchanged.
Both private-index endpoint reductions remain valid, since
the new term in (4) is independent of those indices.

On a segment with fixed \(z,\lambda_b\), the additional
term in (4) integrates from \(d_0\) to \(d_1\) to
\[
                       \frac{\pi}{3}\lambda_b^2(d_1^2-d_0^2).
 \tag{15}
\]
Here the comparison at height zero is a lower bound on the
original force; it does not replace the actual reference
or erase the neighbor's height change from the source.
All original marginal and relative-pinning terms are retained.

This corollary concerns the regular two-incidence force.
The true last row retains its distinct credit from the
neighbor-height theorem. Interior high physical profiles,
the following factor's complete finite-source eligibility,
and the sign of the remaining calibrated comparison are
not asserted by (3)--(15).
