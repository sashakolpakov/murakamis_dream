# Sharpness of the carry-current exponent at an actual crossing

Private written proof, 19 November 2026.

One positive physical crossing can turn an exponentially small
normalized carry current into an exponentially growing one. The exact
calculation uses a single capped input and a single surviving transfer.
Its exponential base equals the positive-majorant base in W below.
There is therefore no transfer-phase cancellation to recover on this
row. The whole meridian family and its zero-framing line remain exact.

This is a test of free coherent kernel domains. It neither places the
displayed coordinates on a faithful geometric fixed graph nor asserts
that the current has a nonzero original closed contraction.

## 1. The literal current and crossing

Use the sole complete direct W, pinned below. Set
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad M=e^\mu,\quad x=-M/q.
 \tag{1}
\]
The quantum root is fixed as \(\mu\) varies. On each physical head,
\[
 Fe_a=(1-Q^{a+1})e_{a+1},\qquad Ke_a=xQ^{-a}e_a,
 \qquad 0\le a\le d,
 \tag{2}
\]
where the top raising arrow is zero. On two heads put
\[
 F_{12}=F_1+K_1^{-1}F_2,\quad J e_{a,b}=(a+b)e_{a,b},
 \quad \Pi_0=\mathbf1_{J\le d},\quad \Pi_d=\mathbf1_{J=d}.
 \tag{3}
\]
Degree conservation at the cut gives the exact identity
\[
                   [F_{12},\Pi_0]=F_{12}\Pi_d.
 \tag{4}
\]
Indeed both orders agree except on input degree \(d\), where raising
leaves the low sector. The actual upper zeros in (2) stay in (4).

Write the positive checked crossing, including its common scalar, as
\[
 R^+(M)=\kappa(M)PD\sum_{n=0}^{d}
       \frac{(-1)^nq^{n^2}}{(Q;Q)_n}E_1(M)^nF_2^n,
 \qquad De_{a,b}=x^{-a-b}Q^{ab}e_{a,b}.
 \tag{5}
\]
Here \(P\) flips the two heads and
\(E(M)e_a=(MQ^{-a}-M^{-1})e_{a-1}\) for \(a>0\), with
the actual bottom-zero arrow. W proves (5) for the whole meridian
family. The computation below only uses its zero-transfer term.

For any finite matrix \(A\), fix the input-binomial convention
\[
 K_A(z,w)=\sum_{a,b,c,e=0}^{d}A_{(c,e),(a,b)}
       \binom da\binom db z_1^cz_2^e w_1^aw_2^b,
 \quad I_N=(1+z_1w_1)^d(1+z_2w_2)^d.
 \tag{6}
\]
All normalized kernels below require the two displayed incidence
factors to be nonzero. Products of matrices are performed before
their kernels are normalized.

## 2. An exact row, its scalar, and every meridian jet

Set \(w_1=0\). In (4),(6), the threshold \(a+b=d\) then
leaves exactly the input \((a,b)=(0,d)\), with binomial weight one.
The second raising term is capped, so
\[
 F_{12}e_{0,d}=(1-Q)e_{1,d}.
 \tag{7}
\]
In (5) on \(e_{1,d}\), every \(n>0\) is killed by the second
head's top cap. Consequently
\[
 R^+(M)e_{1,d}=\kappa(M)x^{-N}Q^d e_{d,1}.
 \tag{8}
\]
Equations (6)--(8) prove, at every level in the actual meridian family,
\[
 \boxed{\left.
 \frac{K_{R^+(M)[F_{12}(M),\Pi_0]}}{I_N}
 \right|_{w_1=0}
 =\kappa(M)x^{-N}Q^d(1-Q)z_2
       \left(\frac{z_1w_2}{1+z_2w_2}\right)^d.}
 \tag{9}
\]
No odd-level, prime-level, or interior-occupation assumption was used.
In particular (9) includes \(N=2\). No cyclic endpoint or omitted
transfer is introduced by the calculation.

For the standard zero-framed crossing, W gives
\[
 \alpha=\kappa x^{-d},\qquad
 \overline R^+=\alpha^{-1}R^+=\kappa^{-1}x^dR^+.
 \tag{10}
\]
Thus the normalized zero-framed current \(\mathcal C_N\) in (9) is
\[
 \mathcal C_N(z_1,z_2,w_2;\mu)
 =x^{-1}Q^d(1-Q)z_2
       \left(\frac{z_1w_2}{1+z_2w_2}\right)^d,
 \qquad \partial_\mu^k\mathcal C_N=(-1)^k\mathcal C_N.
 \tag{11}
\]
For every integer \(k\ge0\), these are the true fixed-\(q\),
fixed-coordinate derivatives of the
original moving matrices and framing line. Since \(x=x_0e^\mu\),
the derivative assertion follows from the exact whole-family identity,
not from differentiating a root specialization. Any further outside
line must still multiply (11) before taking its derivatives.

## 3. Sharp exponential base and an open-domain limitation

For comparison, the same threshold before the crossing gives exactly
\[
 \left.\frac{K_{[F_{12},\Pi_0]}}{I_N}\right|_{w_1=0}
 =(1-Q)z_1
       \left(\frac{z_2w_2}{1+z_2w_2}\right)^d.
 \tag{12}
\]
For \(v_i=z_iw_i\), define the original interface base
\[
 \Gamma(z,w)=
 \frac{(\sqrt{|v_1|}+\sqrt{|v_2|})^2}
 {|1+v_1|\,|1+v_2|}.
 \tag{13}
\]
W's positive crossing map is
\(U_+(s_1,s_2)=(s_2+2s_1,s_1)\). Its composed base is therefore
\[
 \mathcal B_+(z,w)=
 \frac{\bigl(\sqrt{(|z_2|+2|z_1|)|w_1|}
                  +\sqrt{|z_1w_2|}\bigr)^2}
 {|1+z_1w_1|\,|1+z_2w_2|}.
 \tag{14}
\]
On the row in (9), these reduce to
\[
 \Gamma_0=\frac{|z_2w_2|}{|1+z_2w_2|},\qquad
 B_0=\mathcal B_+|_{w_1=0}
       =\frac{|z_1w_2|}{|1+z_2w_2|}.
 \tag{15}
\]
If \(z_1z_2w_2\ne0\) and \(1+z_2w_2\ne0\), (11) gives
\[
 |\partial_\mu^k\mathcal C_N|
   =e^{-\operatorname{Re}\mu}\,2\sin(\pi/N)|z_2|B_0^d.
 \tag{16}
\]
Since \(N\sin(\pi/N)\to\pi\), this has exponential rate
\(\log B_0\), uniformly on compact subsets of that row and on
\(|N\mu|\le\eta\) for each fixed \(\eta\). The polynomial
prefactor cannot change the rate. Thus W's base is attained by an
actual normalized composed Ward kernel, including all its true jets.

For a concrete domain calibration, take
\[
                    (z_1,z_2,w_1,w_2)=(3,1,0,1).
 \tag{17}
\]
Then \(\Gamma_0=1/2\) and \(B_0=3/2\). The uncomposed row
(12) decays exponentially; the zero-framed composed row (11) grows
exponentially. By continuity, (17) has an ambient complex open
neighborhood on which both incidences are units and
\(\Gamma<1<\mathcal B_+\). Its \(w_1=0\) slice contains an open
set of the growing rows (16). Consequently no uniform exponential
decay estimate for the composed current can hold on that neighborhood.
This does not assert pointwise growth at every point with \(w_1\ne0\).

The obstruction is a literal finite composition: one input, one arrow,
and one transfer. Cancellation among crossing phases cannot improve
its exponential base. A stronger theorem may use further matched
geometric conditions, but those conditions cannot be omitted in favor
of \(\Gamma<1\) on the free external kernel coordinates.

## 4. Presentation dependence and the closing-source scope

For \(m\ge2\) heads, there is also an elementary limitation of W's
coarser two-sided base
\[
 \Omega_{m,c}(\tau)=3^c\frac{m^m}{(m-1)^{m-1}}
                        \frac{\tau}{(1-\tau)^m},
 \qquad \tau=(\max|z_j|)(\max|w_j|).
 \tag{18}
\]
Insert \(h\) adjacent inverse crossing pairs in a fixed word. The
actual whole-\(M\) word, its writhe, its zero-framing line and all its
derivatives are unchanged. Its displayed crossing count increases
from \(c\) to \(c+2h\), so (18) is multiplied by \(3^{2h}\).
At any fixed \(0<\tau<1/(m-1)\), this eventually exits the sufficient
domain \(\Omega<1\). Thus that sufficient domain is presentation
dependent. This observation does not forbid simplifying the word or
using a different coordinate chart.

Neither (16) nor the padding calculation identifies these free kernel
coordinates with a faithful geometric point. When \(m\ge3\), W's
sharper base permits uncontrolled spectators: for fixed other coordinates,
sending the two current-pair input coordinates to zero sends its
numerator to zero while spectator incidence factors can remain fixed.
It therefore has no automatic all-head smallness consequence.

The remaining geometric task is to match the actual closed source and
its relative cycle to a domain with a proved composition estimate, or
to obtain a phase-sensitive estimate on that matched cycle. The present
calculation proves no lower bound for a closed period and no counterexample
to finite exceptions. The original closing coupon, scalar lines, and
any later contractions must still be retained.

## Complete proof direct

* W: `notes/research_actual_word_carry_current_composition.md` (496 lines),
  SHA256 `d7c9179a36ac9c9d96c3eb1f8db1e492e6b5a67b3ea56de34cffa57bc926a613`.

The complete direct was freshly whole-read nontruncated in this author
sequence. All new calculations are written finite proofs; no mathematical
programs, tests, or builds were used. Frozen and public files were untouched.
