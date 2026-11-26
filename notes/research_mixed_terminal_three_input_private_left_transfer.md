# A bounded force overshoot on the terminal private left face

Research deduction and fixed saved-data protocol, 6 November 2026.
A small positive terminal force can be paid from an existing main
budget; strict contraction of its negative force is unnecessary.
No new logarithm, root, source, optimizer, or parameter evaluation is
used below. The final saved-data verification has not been run.

## 1. Original stationary force and explicit domain

Use terminal type four and preceding ordinary type four, with either
incoming flag. Write
\[
 a_*=A+ic,\quad t_*=x+ih,\quad e_*=E+ij,\quad
 \bar a=A+iH,\quad e_0=27/100.
\tag{1}
\]
The sufficient reference domain is
\[
 \begin{gathered}
 2987/10000\le x\le7/20,\quad
 -713/10000\le h\le-1/50,\quad603/2000\le A\le9/25,\\
 333/1000\le E\le363/1000,\quad
 -51/1000\le j\le-19/1000,\quad1/100\le H\le7/500.
 \end{gathered}
\tag{2}
\]
Retain the original canonical equations and logarithmic lifts, and put
\[
 \begin{split}
 A_t&=\Re\{g'(t_*+\bar a)-g'(t_*+a_*)\}-2\pi(H-c),\\
 d_L&=\Re\{g'(t_*+e_0)-g'(t_*+e_*)\},\qquad F=A_t+d_L.
 \end{split}
\tag{3}
\]
Lemma 1 of the
[uniform-force proof](research_mixed_terminal_private_left_uniform_force.md)
gives \(d_L>0\) on (2): both summed real arguments lie between
\(1/2\) and \(3/4\); lowering \(E\) to \(e_0\) and raising
its negative height to zero both increase the squared modulus.

Original terminal-index stationarity gives exactly
\[
 F=\Re\{g'(t_*+\bar a)+g'(t_*+e_0)-3g'(t_*)\}-2\pi H.
\tag{4}
\]
For \(r=e^{2\pi h}\), \(R=e^{-2\pi H}\), this means
\[
 e^{2F}=
 \frac{\{R^2+r^2-2Rr\cos2\pi(x+A)\}
       \{1+r^2-2r\cos2\pi(x+e_0)\}}
      {\{1+r^2-2r\cos2\pi x\}^3}.
\tag{5}
\]
The factor \(R\) retains the original chirp. Equation (4) is
asserted only at the actual stationary reference, never at an
enclosing midpoint. Its right-side estimate below holds throughout
the displayed reference rectangle.

## 2. A uniform upper bound \(F<1/50\)

Using \(157/50<\pi<22/7\), (2) implies
\[
 r>63/100,\quad r<1,\quad R<47/50,\quad
 -\cos2\pi x>3/10,\quad
 -\cos2\pi(x+A)<81/100,\quad
 -\cos2\pi(x+e_0)<91/100.
\tag{6}
\]
Here are explicit rational witnesses. Set
\[
 X=76459/250000,\quad Y=78657/125000,\quad
 Z=107859/250000,\quad W=7843/17500,\quad z=157/2500.
\tag{7}
\]
Then
\[
 \begin{split}
 X-X^3/6&>3/10,\\
 1-Y^2/2+Y^4/24&<81/100,\\
 1-Z^2/2+Z^4/24&<91/100,\\
 1+W+\frac{W^2}{2(1-W/3)}&<100/63,\\
 1+z+z^2/2&>50/47.
 \end{split}
\tag{8}
\]
In fact \(X=(2(.2987)-.5)(157/50)\),
\(Y=(2(.2987+.3015)-1)(157/50)\), and
\(Z=(2(.2987+.27)-1)(157/50)\).
The sine is increasing and the summed negative cosines decrease
on the relevant subintervals of \((.5,.75)\).
The alternating trigonometric bounds prove their three inequalities.
The positive exponential series proves the other two, since
\(2(.0713)\pi<W\) and \(z<.02\pi\).

Define
\[
 \begin{split}
 D(r)&=(1+r^2+(3/5)r)^3,\\
 N(r)&=(r^2+(3807/2500)r+2209/2500)
                            (1+r^2+(91/50)r),\\
 P(r)&=(26/25)D(r)-N(r).
 \end{split}
\tag{9}
\]
Both numerator comparisons in (5) have the correct direction:
the first factor increases in \(R\) because its cosine is negative.
Thus \(e^{2F}<N(r)/D(r)\). In ascending powers of \(r\), the
coefficients of \(P\) are the exact terminating decimals
\[
 (.1564,-1.258952,-.411896,.62584,3.2432,1.872,1.04).
\tag{10}
\]
On \([.63,1]\), discard the positive fourth- and fifth-degree
terms of \(P'\), and use \(r\ge3/5\), \(r\le1\). This gives
\[
 P'(r)>-63/50-21/25+(9/5)(3/5)^2+12(3/5)^3=57/50>0.
\tag{11}
\]
Exact substitution gives
\[
 P(63/100)=1474709079737/12500000000000>1/10.
\tag{12}
\]
Consequently
\[
                  F<\tfrac12\log(26/25)<1/50.
\tag{13}
\]
No assertion that \(F<0\) on the entire rectangle is needed.

## 3. A fixed debit instead of strict force contraction

Now fix \(H=1/100\). The
[private-left localization and curvature theorem](research_mixed_terminal_private_left_symmetric_transfer.md)
puts every face maximum in \(.22<t_R<.4\). Its symmetric pair
decomposition holds also for incoming flag zero: only the discarded
zero-force incoming cost changes, as proved by
[the incoming-type transfer](research_mixed_terminal_incoming_type_transfer.md).
Both full-\(P\) Fourier alternatives and all independent targets
remain unchanged.

Let \(G_t(f)\) be the exact conjugate of the retained terminal
convex cost, centered at the true \(x\), on the containing
displacement interval \([.22-x,.4-x]\). The cost is nonnegative
and vanishes at zero. Equations (3) and (13) imply
\[
 G_t(A_t+d_L)\le G_t(A_t)+
 \frac1{50}\left(\frac25-\frac{2987}{10000}\right)
                 =G_t(A_t)+\frac{1013}{500000}.
\tag{14}
\]
Indeed, if \(F\le0\), its maximizing displacement is nonpositive.
The conjugate is nonincreasing on negative forces, so
\(G_t(F)\le G_t(A_t)\), since \(d_L>0\).
If \(F>0\), negative displacements give a nonpositive value,
while positive ones give at most \(F(.4-x)<(.4-x)/50\);
also \(G_t(A_t)\ge0\). No sign of \(A_t\) is assumed.

The original
[joint transfer identity](research_mixed_terminal_private_left_joint_transfer.md)
changes only the lifted trial value by \(E_L\le U_L\), and the
terminal force by \(d_L\). Thus, for either \(\nu=1,0\),
\[
 \sup D_\nu^L\le
          \mathfrak M_{1,\nu}+U_L+\frac{1013}{500000}.
\tag{15}
\]
Here \(\mathfrak M_{1,\nu}\) is any proved same-reference,
same-height main three-cost upper; its first subscript is the
terminal flag. The existing moving-center cubic majorants dominate
the exact gains used in this argument, so (15) needs no new gain call.

In particular the sufficient guards
\[
 \mathfrak M_{1,1}<-33/5000,\qquad
 \mathfrak M_{1,0}<-3/200,\qquad U_L<0
\tag{16}
\]
imply a common strict raw private-left loss \(1/250\).
This finite-source implication is restricted to the original actual
\(K_3\) or \(K_4\) family and its oriented/inverse-feasible
source domain. The force implication holds on any entire auxiliary
canonical family satisfying (2). No other real-cut label is resolved.

## 4. Fixed saved-only verification, not yet executed

Use only the \((\beta,\epsilon)=(0,1)\) case of the completed
record research-mixed-terminal-three-input-budget.json.gz, SHA256
18f5260f3fcd18461d8dd2859d515d9c5180f53127e917debd628ebcf26a0dec.
A standalone standard-library checker must be reviewed before its
single execution. Its fixed inventory is:

1. Bind this proof, the original force, curvature and transfer
   proofs, the completed driver, its independent saved audit, and
   all inherited inputs; verify hashes before and after.
2. Check all exact saved reference guards (2) at \(H=.01\),
   and retain the original selected-height and typed domains.
   Verify the private-left family-2 association with that same
   refined reference and its original actual-source cover.
3. Check all five rational inequalities (8), the polynomial identity
   (9)--(10), the coefficient comparisons in (11), and (12).
4. Read the two unchanged main uppers and the same family's bare
   \(U_L\), verify (16), and recombine (15), checking both strict
   losses exceed \(1/250\).

There are no analytic evaluations, parameter cells, roots, radius
choices, scalar-gain calls, or retries. The earlier failed strict
force guards and positive plane bounds remain unchanged. Until the
saved check is complete, this is a proved criterion, not a reported
new certificate. It makes no whole-source or knot-family claim.
