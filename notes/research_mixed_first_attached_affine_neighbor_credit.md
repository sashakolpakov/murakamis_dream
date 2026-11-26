# An index-dependent credit preserving the coupled endpoint reduction

Research deduction, 7 November 2026. The favorable neighbor-height
credit can be retained as an affine function of the first ordinary
index. The resulting lower expression still reduces to its two
index endpoints. For a first cap of type three, each of those
credited endpoint expressions strictly decreases along the whole
early real interval. Its worst first coordinate is consequently
\(x=\min\{z,.22\}\).

These are statements about the exact conservative lower expression.
No remaining endpoint value or complete boundary sign is assumed.

## 1. A stronger credit that preserves the index structure

Keep the actual source, coefficients and following regular profile
of the
[neighbor-height theorem](research_mixed_first_attached_neighbor_height_credit.md)
and its
[uniform-credit corollary](research_mixed_first_attached_uniform_neighbor_credit.md).
In particular,
\[
 \begin{gathered}
 d=x-.1,\quad .1\le x\le.22,\quad x\le z\le.5,\quad
 b=z-i\lambda_b d,\quad 0\le\lambda_b\le17/20,\\
 .22\le v\le.4,\qquad
 t=w+i\zeta,\quad .22\le w\le.49,\quad -.108\le\zeta\le.068 .
 \end{gathered}                                                \tag{1}
\]
Both \(b\) incidences remain in
\[
 B(v,t;z,h)=
 \Im\{g'(v+z+ih)+g'(t+z+ih)-3g'(z+ih)+2\pi it\}.
 \tag{2}
\]

**Lemma 1.** On the full height interval \(-.108\le h\le0\),
\[
 -\frac1\pi\partial_h B>
                     L(v):=\frac{10}{3}v-\frac5{87}.
 \tag{3}
\]
Hence, at the same actual correlated height,
\[
 \lambda_b B(v,t;z,-\lambda_b d)
 \ge \lambda_b B(v,t;z,0)+\pi L(v)\lambda_b^2d .
 \tag{4}
\]

*Proof.* For \(z\ge.28\), the proof of the uniform-credit
corollary gives the sharper bound
\[
 -\partial_hB/\pi\ge
             m(v):=\frac{\sin(2\pi v)}{5/4+\cos(2\pi v)} .
 \tag{5}
\]
It suffices to prove \(m(v)>L(v)\).
Writing \(C=5/4\), the second derivative of \(m\) has the sign
of
\[
                       2+C\cos(2\pi v)-C^2 .
 \tag{6}
\]
It changes from positive to negative once on \([.22,.4]\),
at \(\cos(2\pi v)=-7/20\).
Furthermore
\[
 m'(.22)>
      \frac{6(49/40)}{(29/20)^2}
                         =\frac{2940}{841}>\frac{10}{3}.
 \tag{7}
\]
Here \(9/50<\sin(.06\pi)<1/5\); the lower inequality
follows from \(\sin u\ge u-u^3/6\),
\(.06\pi>471/2500\), and \(.06\pi<1/5\).
The factor \(6\) in (7) uses \(2\pi>6\).
Thus \(m-L\) initially increases, and its derivative can
cross zero only from positive to negative. Its minimum is
at an endpoint. The existing endpoint bounds give
\[
 \begin{split}
 m(.22)&>98/145=L(.22),\\
 m(.4)&>58/45>37/29=L(.4).
 \end{split}                                                  \tag{8}
\]
This proves (3) for \(z\ge.28\).

For the lower real intervals use the exact cotangent estimates
in the uniform-credit corollary.
On \(.1\le z\le.15\), its constant floor \(254/201\)
pays every \(v\le.35\), since \(L(.35)=193/174<254/201\).
For \(v\ge.35\), the first shifted real argument is at least
\(.45\), whose real cotangent is less than \(1/6\);
the following one is still less than \(2/3\).
The force floor is therefore
\[
                       174/67-5/6>37/29.
 \tag{9}
\]
For the elementary bound at \(.45\), use
\(.05\pi<11/70\) and
\(\tan(.05\pi)<(11/70)/(1-(11/70)^2/2)<1/6\).
On \(.15\le z\le.2\), the old floor \(29/19\)
already exceeds \(37/29\).
On \(.2\le z\le.28\), use the old floor \(104/87\)
for \(v\le.3\), since \(L(.3)=82/87\).
For \(v\ge.3\), the first shifted real cotangent is
nonpositive and the following one is less than \(1/3\);
the resulting floor is
\[
                         54/29-1/3=133/87>37/29 .
 \tag{10}
\]
This exhausts the domain. Integrating (3) proves (4),
including the zero-height and zero-coefficient cases. \(\square\)

## 2. The four endpoint lower expressions

Let \(H_\alpha(e,v;x,\lambda_a)\) be the original first-coordinate
derivative (12) in the neighbor-height theorem. Define
\[
 \begin{split}
 T(z,t)&=\pi(-1+2z+2w)
       +\arg(1-e^{2\pi\zeta}e^{-2\pi i(w+z)}),\\
 \underline{\mathcal H}_\alpha(e,v)
 &=H_\alpha(e,v;x,\lambda_a)-\pi\lambda_bv
                    +\lambda_bT(z,t)+\pi L(v)\lambda_b^2d .
 \end{split}                                                  \tag{11}
\]
The argument is on the original lift.
The actual regular coupled derivative is at least (11), plus
the separate favorable first-index-height credit.
This follows from the exact identity
\(B(v,t;z,0)=T(z,t)-\pi v\), not from replacing the
neighbor's two factors by an independently calibrated source.

Put
\[
             \widetilde\lambda_b
                =\lambda_b-\frac{10}{3}\lambda_b^2d .
 \tag{12}
\]
Since \(\lambda_bd\le51/500\),
\[
       0\le\widetilde\lambda_b\le\lambda_b\le17/20 .
 \tag{13}
\]
The \(v\)-dependent part of (11) is precisely
\[
                    H_\alpha(e,v)-\pi\widetilde\lambda_bv .
 \tag{14}
\]
Thus Lemma 2 of the neighbor-height theorem applies unchanged,
with \(\widetilde\lambda_b\) replacing its free nonnegative
coefficient. The minimum is at \(v=.22\) or \(v=.4\).
The private endpoint reduction is unchanged:
\[
 e=.27,.49\quad(\alpha=0),\qquad
 e=.27,.4\quad(\alpha=1).
 \tag{15}
\]
This legitimately retains the different credits in (8) in
the four endpoint expressions. A nonlinear credit may not
simply be inserted after an endpoint minimization; (12)--(14)
are the reason that this particular improvement is valid.

## 3. For a first type-three cap the worst \(x\) is an endpoint

Now assume \(\alpha=0\), so
\(-7/40\le\lambda_a\le3/5\), with its original radius
\(r=e^{-2\pi\lambda_a(x-.1)}\).
Hold \(z,t,\lambda_a,\lambda_b,e,v\) fixed.
This preserves the coefficient-radius correlations.

**Proposition 2.** At either \(e\) endpoint in (15) and
either \(v\) endpoint in (14),
\[
              \frac{d}{dx}\underline{\mathcal H}_0
                                      <-\frac{3\pi}{50}<0.
 \tag{16}
\]
Therefore the worst value on the actual first-minimum
interval is at \(x=\min\{z,.22\}\).

*Proof.* Write
\[
 \begin{split}
 P&=2\Re\cot\pi a-\Re\cot\pi(e+a)-\Re\cot\pi(v+a),\\
 Q&=\Im\cot\pi(e+a)+\Im\cot\pi(v+a)-2\Im\cot\pi a .
 \end{split}                                                  \tag{17}
\]
Direct differentiation of the original logarithms gives
\[
              \partial_xH_0=-\pi(1-\lambda_a^2)P
                                             +2\pi\lambda_aQ.
 \tag{18}
\]
The own angular cosine is positive, while both shifted
angular cosines are negative throughout these intervals.
All three imaginary cotangents
have the same signed hyperbolic numerator. Each shifted
one has smaller modulus than the own one.
Consequently \(Q\) has the sign opposite to \(\lambda_a\),
or is zero. Hence \(\lambda_aQ\le0\).

The common-radius cotangent bounds in the
[own-four moving comparison](research_mixed_first_four_moving_height_comparison.md),
Section 2, apply also to this smaller height range:
\[
 \Re\cot\pi a>147/143,\qquad
 \Re\cot\pi(e+a)<1/2,\qquad
 \Re\cot\pi(.22+a)<2/3 .
 \tag{19}
\]
They use only \(3/5<r<23/20\) and
\((r+r^{-1})/2<17/15\), which hold here.
Also \(1-\lambda_a^2\ge16/25\).

At \(v=.22\), (17)--(19) give
\[
 -\partial_xH_0/\pi>
       \frac{16}{25}\left(\frac{294}{143}-\frac76\right)
                              =\frac{6104}{10725}>\frac{14}{25}.
 \tag{20}
\]
The derivative of the added credit in (11) is at most
\[
 L(.22)(17/20)^2
                           =\frac{14161}{29000}<\frac12
 \tag{21}
\]
after division by \(\pi\).
All other terms of (11) are constant in \(x\).
Equations (20)--(21) yield (16).

At \(v=.4\), the shifted argument \(v+x\in[.5,.62]\)
has nonpositive real cotangent. Thus
\[
 -\partial_xH_0/\pi>
       \frac{16}{25}\left(\frac{294}{143}-\frac12\right)
                                  =\frac{712}{715}>\frac{99}{100}.
 \tag{22}
\]
The credit derivative is at most
\[
 L(.4)(17/20)^2=\frac{10693}{11600}<\frac{93}{100}.
 \tag{23}
\]
Again their difference exceeds \(3/50\), proving (16).
The actual range with \(z\) fixed is
\(.1\le x\le\min\{z,.22\}\), so its upper endpoint
has the worst value. \(\square\)

The last proposition removes an actual continuous parameter
from the regular own-three lower comparison. It does not
assert that the remaining endpoint values are positive.
For \(z<.22\) the retained endpoint is the diagonal \(x=z\),
not an infeasible replacement by \(x=.22\).
The own-four first coefficient, true ordinary last row and
interior physical-tail alternatives retain their separate
comparisons. Full following-source eligibility, original
middle compensation and the calibrated boundary value
remain part of the source problem.
