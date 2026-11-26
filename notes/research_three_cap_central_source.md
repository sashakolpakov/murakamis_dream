# The full first attachment of an original complete cap

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The full wire period, including the central index and angular currents,
has a nonzero asymptotic after one actual complete cap is attached to a
three-crossing vertex. The proof first treats the corner-deleted vertex,
then restores the original vertex by a source-specific Fourier boundary
estimate. The input is the original finite cap, not a Gaussian substituted
for it. The output is holomorphic near the homogeneous Fourier wire.
This is a first-attachment theorem; no iteration along arbitrary chains
is inferred.

## 1. The original finite source and its local coefficient

Use the exact notation of
[the traced vertex](research_traced_three_vertex_endpoint.md):
\[
 A=JM^3,\qquad \widetilde A=A-E_L,\qquad
 L=\lfloor N/50\rfloor,\qquad
 E_L=M^TP_LJM P_LM,\qquad
 \widetilde V_N(x,y)=h(x)^T\widetilde A h(y).
 \tag{1}
\]
Here \(P_L\) projects onto indices \(0,\ldots,L\). Let
\(v(w)=(e_j(w))_{j=0}^{N-1}\), and write the actual complete cap as
\[
 W_N(x,u)=v(-2\cos u)^TAh(x),\qquad
 x_h=\frac16+\frac{i\log2}{2\pi},\qquad Y_h=\Im x_h.
 \tag{2}
\]
Thus \(u\) is an outside angle; ordinary boundary normals mean
derivatives in the spectral color \(w=-2\cos u\).
The full attachment is exactly
\[
 \begin{split}
 {\cal C}_N(y,u)
 &=N\int_{-1/8+iY_h}^{7/8+iY_h}
                  W_N(x,u)\widetilde V_N(x,y)\,dx\\
 &=v(-2\cos u)^TA\widetilde A h(y).
 \end{split}
 \tag{3}
\]
The second equality is the literal half-band identity
\(N\int h(x)h(x)^Tdx=I\). Both factors have period sign
\((-1)^{N-1}\), so their product is periodic at both parities.

Let \(S(x,u)\) be the actual cap critical phase, and \(\Phi(x,y)\)
the retained-vertex phase, with their original continued constants.
The [certified attachment](research_three_cap_first_attachment.md)
gives the critical point \(x_c\), cap angle \(\tau_c\), and the
continued phase
\[
 \Theta(x;y,u)=S(x,u)+\Phi(x,y),\qquad
 \Theta_{\rm eff}(y,u)=\Theta(x_c(y,u);y,u).
 \tag{4}
\]
At \((y,u)=(x_h,0)\),
\[
 \begin{gathered}
 \Re x_c\simeq .177337918569,\quad
 \Im x_c\simeq .101358689576,\quad
 \tau_c\simeq1.533800710766-.978955098406i,\\
 -\Re\Theta_{xx}(x_c)>21,\qquad
                    \Re\Theta_{\rm eff}(x_h,0)>\frac{19113}{10000}.
 \end{gathered}
 \tag{5}
\]
The exact local packet amplitudes are denoted by \(A_c(x,u)\) and
\(a(x,y)\):
\[
 W_N=C_{N,3}N^{-1}A_c e^{NS}(1+O(N^{-1})),\qquad
 \widetilde V_N=\kappa N^{-1/2}a e^{N\Phi}(1+O(N^{-1})).
 \tag{6}
\]
Their nonzero constants, branches and parity phases are those in the
proved [cap](research_homogeneous_wire_complete_cap.md) and
[directed retained packet](research_three_vertex_directed_packet.md).

**Theorem 1.** On a fixed complex neighborhood of \((y,u)=(x_h,0)\),
the full finite source (3) satisfies, through every integer level,
\[
 {\cal C}_N(y,u)=C_{N,3}\kappa N^{-1}
 {\cal A}(y,u)e^{N\Theta_{\rm eff}(y,u)}
                         (1+O(N^{-1})),
 \qquad
 {\cal A}=
 \frac{\sqrt{2\pi}\,A_c(x_c,u)a(x_c,y)}
                       {\sqrt{-\Theta_{xx}(x_c;y,u)}}\ne0.
 \tag{7}
\]
The square root is the actual local Gaussian branch. The normalized
remainder is holomorphic and uniformly \(O(N^{-1})\). The assertion
therefore retains all fixed ordinary outside-color derivatives. The
outside dependence is separately even in \(u\), and descends to a
neighborhood of the ramified complete color \(w=-2\).

## 2. Actual angular remainders on the central wire

Put \(h_c=\Im x_c\), \(H_c=-\Im\tau_c\). We use the slightly larger
closed enclosures
\[
 I_h=[.10135867,.10135871],\qquad
 I_H=[.97895508,.97895512],\qquad
 \frac7{50}\le\Re x\le\frac15.
 \tag{8}
\]
The certified root polydisk is strictly inside these intervals.
Use the original double-pole trace with midpoint cuts
\(T_N=41/20+O(N^{-1})\), and lower depth \(H_c\). Its upper rate is
the same exact function as in
[the exterior-cap proof](research_three_cap_wire_complement.md):
\[
 {\cal R}(x,\tau,H)=
 \mathfrak b(x,\tau-iH)+\Re\Psi(\tau-iH)
                        +\frac{3\tau H}{2\pi}-H.
 \tag{9}
\]
All reciprocal-factorial reflection terms are retained. The actual
low complete kernel obeys its logarithmic upper bound throughout this
rectangle, since \(-2\cos(41/20)\cosh H_c<3/2<2\).
The full cap's removed radical is estimated using its original
physical values and normals, as in that exterior proof.

**Lemma 2.** Uniformly on (8), the exact cap has an exponential upper
bound \(253/200=1.265\). After retaining only the positive lower
horizontal interval \(0\le\Re\tau\le9/5\), every remaining angular
integral, folded vertical current and physical tail has upper rate
strictly below \(63/50=1.26\). The removed radical has rate below \(2/3\).
All bounds include polynomial prefactors and every original normal.

*Proof.* The compact certificate bounds (9) by \(253/200\) on
\([0,9/5]\), and by \(63/50\) on the negative bottom, the positive
bottom \([9/5,41/20]\), and both folded verticals. The verticals
are split at the actual moving factorial switch \(H=2\pi h_c\).
The exact midpoint denominators are bounded, including height zero.
The physical omitted rows have rate
\(\mathfrak b(x,41/20)+\Psi(41/20)<63/50\);
the original radical observations have
\(\mathfrak b(x,0)<2/3\). Thus this is a decomposition of the
original trace, with its odd simple node and its first normals.

There are nine angular domains: one principal bottom, six complementary
bottom/vertical pieces, and the physical tail and radical. On the three
bottom pieces the certificate uses the exact real derivatives
\[
 \begin{split}
 \partial_\xi\Re{\cal F}_3
 &=\Re\{\log\cos(\pi x+t/2)+\log\cos(\pi x-t/2)
                                      -2\log\sin\pi x\},\\
 \partial_\tau\Re{\cal F}_3
 &=\Re\left\{
 \frac{\log\cos(\pi x+t/2)-\log\cos(\pi x-t/2)}{2\pi}
 -\frac{\log(\tan(t/2)+\sec(t/2))}{\pi}
                         +\frac{3it}{2\pi}-i\right\}.
 \end{split}
 \tag{10}
\]
These are real derivatives on the original reflected sides; possible
imaginary logarithmic lift constants do not change them. Interval
derivatives bound variation from the exact box center.

At a factorial zero, the primitive is continuous. The elementary
bound used by the exterior proof has the sharper radius-dependent form
\[
 |J_{\rm side}(z)|
 \le r\{-\log(2\pi r)+\pi+1+1/199\},
 \quad |z|\le r\le1/20.
 \tag{11}
\]
It follows by integrating the logarithm radially and using
\(|\sin(\pi z)/(\pi z)-1|<1/200\).
The right side tends to zero. This includes the vertical current
through a factorial zero without introducing a pole or discarding a
reflection term. The certificate and independent replay use (11).
The literal finite-normal and small outside-neighborhood bounds are
exactly those of the exterior-cap proof. \(\square\)

The [global retained bound](research_three_vertex_global_wire_bound.md),
Proposition 4, applies at height \(h_c\), and gives rate \(6474/10000\).
Its proof bounds the absolute value of every original real-index
summand before summing. The identical bound therefore applies to any
real-index subset. Likewise Lemma 2's \(253/200\) bound applies to the
retained positive bottom alone, as well as to the whole cap.
Thus Lemma 2 discards its angular remainder in the full wire integral:
\[
 \frac{63}{50}+\frac{6474}{10000}=1.9074
                <\Re\Theta_{\rm eff}(x_h,0)-\frac3{1000}.
 \tag{12}
\]
The principal bottom keeps the exact original double-pole density.
Its nonconstant trace denominator corrections cost \(e^{-NH_c}\)
and are harmless under the same bounds. No normal is replaced by an
ordinary value in this step.

## 3. The real retained-index complement

Write \(X=e^{2\pi ix}\), \(Y=e^{2\pi ix_h}\). The exact retained
summand has the real upper exponent
\[
 {\cal E}(s,t;x)=
 \Re\{F(s,t;X,Y)-\pi i(x+x_h)\}.
 \tag{13}
\]
This includes both cardinal exponential factors. On real indices,
its leading entropy is continuous on the full closed index triangle;
the original finite factorial estimates have at most polynomial
endpoint losses.

**Lemma 3.** On (8), the original real-index sum outside
\(B^2\), \(B=[1/4,9/20]\), has upper rate strictly below \(16/25=.64\).
The retained corner deletion and every finite endpoint are included.

*Proof.* First restrict \(s+t\le99/100\). The certificate covers,
in both index orders, the following three domains:
\[
 \begin{array}{ll}
 0\le s\le1/50,&1/50\le t\le99/100-s,\\
 1/50\le s\le1/4,&0\le t\le99/100-s,\\
 s=9/20,&0\le t\le99/100-s.
 \end{array}
 \tag{14}
\]
Their union covers every low-index complement. It also bounds every
high-index complement by monotonicity. Indeed put \(r=|X|<27/50\).
For \(9/20\le s\le7/8\) and \(.14\le\Re x\le.20\),
\(1/4\le s-\Re x<3/4\), and hence
\[
 \exp(\partial_s{\cal E})
   =\frac{r\,|1-e^{-2\pi i(s+t)}|}
                    {|1-Xe^{-2\pi is}|}
   \le\frac{2r}{\sqrt{1+r^2}}<1.
 \tag{15}
\]
For \(s\ge7/8\), the same ratio is at most
\(r\pi/[4(1-r)]<1\), since \(s+t\le1\).
The other index has the identical proof, with its fixed wire phase
\(\Re x_h=1/6\). Reducing a high index to \(9/20\) increases the
entropy, proving the reduction to (14).

On the remaining top collar \(s+t\ge99/100\), use
\(\log|X|,\log|Y|<-3/5\), the dilogarithm majorant \(2/3\),
and
\[
 J(s+t)\le\frac{13}{300},\qquad
 \pi(h_c+Y_h)<\frac7{10}.
 \tag{16}
\]
The first estimate follows from
\(-J(\epsilon)\le\epsilon(1-\log(4\epsilon))\),
\(0\le\epsilon\le1/100\), and \(\log25<10/3\).
Thus its full rate is at most
\[
 -\frac35\frac{99}{100}+\frac49+\frac{13}{300}
                               +\frac7{10}<\frac{16}{25}.
 \tag{17}
\]
All comparisons are strict. The floor in \(L=\lfloor N/50\rfloor\)
and the half-grid cuts at \(B+O(N^{-1})\) only change these closed
domains by \(O(N^{-1})\). The uniform finite-product estimate and
the \(r|\log r|\) endpoint modulus give polynomial costs there;
equivalently the strict compact margins persist under a small fixed
enlargement. No original row between the finite cuts is lost.
\(\square\)

The exact source factor \(W_N\) has rate at most \(253/200\) by
Lemma 2. Consequently its product with this discarded real sum has
rate below
\[
 \frac{253}{200}+\frac{16}{25}=1.905
               <\Re\Theta_{\rm eff}(x_h,0)-\frac1{200}.
 \tag{18}
\]
The estimate is made before any index contour deformation.

## 4. Exhausting the central currents and retaining the coefficient

Apply the exact two cotangent residue formulas to the remaining
central indices, with half-grid vertical cuts at the ends of \(B\)
and horizontal heights \(\pm1/50\). The
[independently certified index-current theorem](research_three_attachment_index_currents.md)
keeps all sixteen products of contour sides. Every product containing
a vertical side has vertex rate below \(323/500=.646\); each
nonconstant horizontal cotangent product has rate below
\(7/10-2\pi/50\). After multiplication by the actual cap,
\[
 \frac{253}{200}+\frac{323}{500}=1.911
              <\Re\Theta_{\rm eff}(x_h,0)-\frac1{5000},
 \qquad
 \frac{253}{200}+\frac7{10}-\frac{2\pi}{50}<1.84.
 \tag{19}
\]
Separate maximum principles extend the vertical-side estimates over
the other index rectangle. Thus they also retain every side generated
when the four constant cotangent products are moved to the actual two
index heights. Their combined coefficient is exactly \(+N^2\).

Now keep the positive cap bottom \(0\le\Re\tau\le9/5\) at depth
\(H_c\). Before eliminating any variable, the principal phase is
\[
 {\cal G}(x,\tau,s,t;y,u)=
       {\cal F}_3(x,\tau;u)+F(s,t;x,y)-\pi i(x+y).
 \tag{20}
\]
At \(u=0,y=x_h\), the four imaginary parts are those of the actual
certified critical point. All its real coordinates are strictly inside
the product box. The proved
[joint concavity theorem](research_three_vertex_joint_concavity.md)
therefore gives a strict gap outside every fixed neighborhood of this
point throughout
\[
 \Re x\in[7/50,1/5],\quad
 \Re\tau\in[0,9/5],\quad
 \Re s,\Re t\in[1/4,9/20].
 \tag{21}
\]
This compares the actual joint density with its actual critical value;
no independent modulus maximization of the indices is used in (21).
The factorial and index symbols are uniform there, and the actual low
complete kernel has its polynomial upper bound with exponent
\(\Re\Psi(\tau)\) throughout this box. Its nonzero asymptotic packet
is needed only near the critical point. These give the uniform upper
bound with exponent \(\Re{\cal G}\) on the principal complement.
The trace correction just mentioned is exponentially smaller. Thus
the only surviving leading contribution is the local Gaussian at this
critical point.

To finish the wire cycle, split the original period in (3) into its
central segment and its exterior. The actual exterior has a gap by
[Theorem 1 of the exterior proof](research_three_cap_wire_complement.md).
Deform the central wire segment down to height \(h_c\). Its two
vertical joins have a gap by Proposition 2 of the same note. These
are deformations of the exact finite holomorphic source: the cap trace
may be represented at each wire point by its original contour, without
a trace-height Jacobian term. No periodicity of the off-grid angular
integrand is asserted. The fixed outside ends of the wire period
cancel because the complete product is periodic.

The preceding sequence is exhaustive: exterior and joins; real-index
complement; cap angular/physical/radical remainder; vertical index
products; nonconstant cotangent products; principal joint complement;
and finally the one local critical neighborhood. Its coefficient in
this exact decomposition is \(+1\). Every other term has a strict
exponential gap, so it cannot cancel that coefficient.
In this order the angular remainder is multiplied only by the retained
real-index subset, which is covered by the termwise bound after Lemma 2.
The index side currents are multiplied by the retained positive cap
bottom, which has the same \(253/200\) upper rate. Thus no product of
separately discarded pieces is lost or estimated using a cancellation
that was removed in an earlier step.

Inside a sufficiently small neighborhood, both original packets (6)
are valid uniformly on the actual directed source chart. Their local
wire integral is the independently proved first-attachment Gaussian,
with coefficient (7). This identifies the principal joint calculation
with the literal source normalization, including \(N\,dx\), \(N^2\)
from the index residues, both parities and the original trace scalar.
It proves Theorem 1.

All finitely many complementary bounds are strict on compact sets.
They persist under a small complex change of the outgoing wire and
ordinary outside color. The actual local saddle and its determinant
continue holomorphically, and the contours move inside the same fixed
charts. The original cap normal bounds supply every outside derivative;
no division by \(\sin u\) at the complete point is required. This
proves the asserted holomorphic and ordinary-normal scope.
\(\square\)

## 5. Restoring the original vertex

**Corollary 4.** The original, undeleted finite source
\[
 {\cal B}_N(y,u)=v(-2\cos u)^TA^2h(y)
 \tag{22}
\]
has exactly the asymptotic (7), with the same phase, nonzero coefficient,
parity factors and ordinary outside-normal scope.

*Proof.* The source-specific
[Fourier corner-transfer theorem](research_three_chain_fourier_corner_transfer.md)
retains the actual complete cap and proves
\[
 \begin{split}
 {\cal B}_N-{\cal C}_N
 &=v(-2\cos u)^TAE_Lh(y)\\
 &=\kappa^2(v(-2\cos u)^TM^{-1})H D_N Mh(y),\\
 H&=M^*M,\qquad D_N=\kappa^{-1}ME_LM^{-1}.
 \end{split}
 \tag{23}
\]
On the full line \(\Im y=Y_h\) and real outside colors, its rate is
\[
 2c+\frac{M_\infty}{2}+\frac3{25}+\frac{\log2}{2}
             <\frac{17}{10}
             <\Re\Theta_{\rm eff}(x_h,0)-\frac15.
 \tag{24}
\]
This uses the exact bound
\(\|Mh(y)\|\le\operatorname{poly}(N)e^{N\log2/2}\), obtained from
the actual transformed boundary vector, and the original full-jet
bound on \(v(w)^TM^{-1}\). It is not inferred from a bound for two
ordinary boundaries. The cited theorem proves the same strict
comparison for fixed ordinary outside derivatives and nearby complex
parameters. Adding this exponentially smaller error to Theorem 1
proves the corollary. \(\square\)

## 6. Reproduction and exact scope

The [author certificate](../experiments/certify_three_cap_central_complement.py)
and [saved cover](../repro/results/research-three-cap-central-complement.json)
contain the nine cap domains and six real-index domains above.
Every accepted box is a closed rational binary cell. The
[independent replayer](../experiments/replay_three_cap_central_complement.py)
checks exact multiplicity-one coverage and uses the negative-frequency
dilogarithm for the retained action, and reflection to the positive strip
for the cap factorial primitive. Its
[record](../repro/results/research-three-cap-central-complement-replay.json)
records all accepted/refined cells and strict scalar comparisons.

Run:

~~~sh
python3 experiments/certify_three_cap_central_complement.py --precision 160
python3 experiments/replay_three_cap_central_complement.py --precision 192
~~~

Theorem 1 concerns exactly \(v(w)^TA(A-E_L)h(y)\), as (3) states.
Corollary 4 restores \(v(w)^TA^2h(y)\) using the separately proved
Fourier endpoint error. The output remains a genuine Fourier-boundary
source near \(y=x_h\); it is not a complete-ended knot closure.
No arbitrary-chain nonzero coefficient or whole-period decay of the
newly produced cap is inferred here.
