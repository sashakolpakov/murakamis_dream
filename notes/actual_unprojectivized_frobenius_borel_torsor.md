# An actual unprojectivized Frobenius source is a marked Borel torsor

Research proof and independent audit, 27 October 2026. The actual
high-color coherent source, its scale character, and one first
descendant recover the complete framing two-form explicitly.
The scale must be retained before normalizing the projector.
A marked Kummer cover is necessary: the actual Sym^N data know
the N-th power of that scale, not its unmarked root.

This is a source/framing moment map. It does not yet intertwine the
full network Gaussian coefficients or prove the selected volume norm.

## 1. Original divided matrices give the whole coherent source

Use the actual high integral color with r=N and the root
Frobenius matrices e,f,h:
\[
 ev_k=(N-k+1)v_{k-1},\quad fv_k=(k+1)v_{k+1},\quad
 hv_k=(N-2k)v_k .
\]
The pure-power source is
\[
 \psi(a,b)=\sum_{k=0}^Na^{N-k}b^kv_k .
\]
Its exact root differential laws are
\[
 e\psi=b\partial_a\psi,\quad
 f\psi=a\partial_b\psi,\quad
 h\psi=(a\partial_a-b\partial_b)\psi .                 \tag{1}
\]
Thus this is the actual Sym^N source cone, not an auxiliary
representation.

It also has a specified ORIGINAL whole q-germ on every residue
string s:
\[
 \psi_s(q;a,b)=
   \sum_{k=0}^N\frac{a^{N-k}b^k}{k!}
                              (F^{(N)}(q))^kw_{0,s}.
\]
The divided matrices have regular integral Gaussian entries, so
this is polynomial in a,b and regular in q, including a=0.
The corresponding whole duals use the actual
\(\exp(u\tau E^{(N)}(q))\), with their actual pairing units retained.
The linear SL2 formulas (1) are root formulas; their full normal
deformations are the actual bounded-PBW operators already proved.

The distinguished fixed root co-source is
\(\lambda_+(v_k)=2^{-N}\binom Nk\). Its scale pairing is
\[
                 \lambda_+\psi(a,b)=((a+b)/2)^N.      \tag{2}
\]
Normalizing by this quantity is legitimate only off its source
wall and must not erase the character or its quantum derivatives.

## 2. Retain the scale AND the contragredient dual flag

For the actual cut-Borel generators
\[
 M_1=h+2f,\qquad M_2=e+f ,
\]
the standard ket \(w_+=(1,1)^t\) is an eigenvector of BOTH.
Its vector cone alone has a one-dimensional orbit at that anchor.
The correct paired source retains its contragredient dual flag.

Write the standard ket and dual as
\[
 w=\alpha(1,1)^t,\qquad
 \ell=\frac{(1,u)}{\alpha(1+u)},\qquad \ell w=1 ,
 \quad \alpha\ne0,\quad u\ne-1 .
\]
Their ACTUAL Sym^N source and normalized co-source are
\[
 \psi_\alpha=\alpha^N\sum_kv_k,\qquad
 \lambda_{\alpha,u}(v_k)=
       \frac{\binom Nk u^k}{\alpha^N(1+u)^N}.          \tag{3}
\]
They pair to one. These are the source vector and co-source
separately, not only their scale-invariant rank-one projector.

Let g preserve the projective ket line \(w_+\), act on w by g,
and on the dual by \(\ell g^{-1}\). Direct differentiation gives
\[
 Y_1=\alpha\partial_\alpha+2u(1+u)\partial_u,\qquad
 Y_2=\alpha\partial_\alpha+(u^2-1)\partial_u .         \tag{4}
\]
These have rank two at \((\alpha,u)=(1,1)\).
The normalized projector alone would forget alpha and lose that
direction.

Here u is an affine flag chart. Include u=infinity as well:
in the global affine coordinate m=(1-u)/(1+u), write
\[
 \ell=\frac{(1+m,1-m)}{2\alpha},\qquad
 \lambda_{\alpha,m}(v_k)=\alpha^{-N}\binom Nk
       \left(\frac{1+m}{2}\right)^{N-k}
       \left(\frac{1-m}{2}\right)^k .
\]
These formulas are regular for every m in A^1, including m=-1
(the chart point u=infinity). The FULL marked paired space is
G_m times A^1; the displayed finite-u chart alone is not
preserved by every Borel element.

This full space is genuinely a Borel torsor on the STANDARD marked cover.
A group element fixing w and its normalized dual fixes the
complementary dual kernel as well; determinant one then forces
identity. The Borel has the same dimension as this open paired
source space and acts transitively: scale w, then use its unipotent
subgroup to move the dual with its fixed nonzero pairing.
Equivalently use \(m=(1-u)/(1+u)\); (4) become
\[
 Y_1=\alpha\partial_\alpha+(2m-2)\partial_m,\qquad
 Y_2=\alpha\partial_\alpha+2m\partial_m ,
\]
the ordinary free affine Borel action on \(\mathbb G_m\times\mathbb A^1\).
More explicitly, in the standard basis
\(w_+=(1,1),w_-=(1,-1)\), the unique group element from
the reference \((\alpha,m)=(1,0)\) is
\[
       g(\alpha,m)=
          \begin{pmatrix}\alpha&-m/\alpha\\0&\alpha^{-1}\end{pmatrix}.
\]
It sends the ket to the stated ket and the reference dual
contragrediently to the stated dual.

## 3. The exact equivariant internal-frame map

For constants \(C\ne0,D\), put
\[
       s=C\alpha^2,\qquad
       r=\frac1{1+u}+D\alpha^2,\qquad A=\frac1{1+s}.   \tag{5}
\]
The regular A/Omega_cut chart additionally requires
1+C alpha^2!=0. The framing map and invariant Haar form have
their stated rational meanings on the larger open alpha!=0,
u!=-1; the cut-density pole is retained at the omitted divisor.
The letter r here is the framing coordinate; the color highest
weight was fixed to N. Calculation in (4) gives
\[
 Y_1(r)=2(r-1),\quad Y_2(r)=2r-1,\quad
 Y_1(s)=Y_2(s)=2s .
\]
Thus the actual paired-source Borel fields map EXACTLY to
\[
 \xi_1=2(r-1)\partial_r+2s\partial_s,\qquad
 \xi_2=(2r-1)\partial_r+2s\partial_s,                 \tag{6}
\]
the original compensated cut-framing fields.
The map has nonzero local Jacobian on this open set.
It is a marked sign cover of the PGL2 framing torsor, not an
identification of every Fr generator with an old head current.

Choose \(C=-2,D=0\). The actual source anchor
\((\alpha,u)=(1,1)\) maps to
\[
                 (r,s)=(1/2,-2),\qquad A=-1.
\]
It is a regular frame with nonzero Borel fields.
This repairs the vanishing-vector obstruction of the normalized
compact Fr projector at its anchor.

The original complete meridian signs, full peripheral dimension
line, and half-form marks remain separate. Formula (5) does not
equate the OLD physical clock with the new diagonal Q^R clock;
the controlled Fourier polarization dictionary is still required.

## 4. A scale character and ONE actual descendant give the full two-form

The Berry form of (3) is
\[
                \lambda_{\alpha,u}d\psi_\alpha=N\,d\log\alpha .
\]
Its curvature is zero on this Borel. It must NOT be called the
framing area form.

The missing covector comes from an actual first descendant:
\[
 U=\lambda_+\psi_\alpha=\alpha^N,\qquad
 m=\frac1N\lambda_{\alpha,u}h\psi_\alpha
                                  =\frac{1-u}{1+u}. \tag{7}
\]
Both are literal source/co-source pairings of original divided
matrices. Define
\[
 \omega_H=\frac1N d\log U=d\log\alpha,\qquad
 \omega_U=-\frac{dm}{2\alpha^2}
                    =\frac{du}{\alpha^2(1+u)^2}.
\]
They satisfy \(d\omega_H=0\),
\(d\omega_U=-2\omega_H\wedge\omega_U\), the explicit
Borel Maurer differential law.

The invariant Haar form and the actual compensated framing form
are respectively
\[
 \widehat\Omega=-\frac{dr\wedge ds}{s^2},\qquad
 \Omega_{\rm cut}=-\frac{dr\wedge ds}{s(1+s)} .
\]
Substitution of (5) gives the exact source identities
\[
 \widehat\Omega=-\frac2C\,\omega_H\wedge\omega_U,
 \qquad
 \boxed{\ \Omega_{\rm cut}=\frac A N\,d\log U\wedge dm\ }. \tag{8}
\]
The constant D drops out. Hence the rank-two co-source form is
recovered from SCALE plus DESCENDANT, not from Berry curvature.
Its covariance under (6) is exactly
\(\operatorname{div}_{\Omega_{\rm cut}}\xi_i=2A\).
The Haar form instead is invariant. This retains the source-density
correction needed by the actual geometric Ward currents.

For C=-2, the exact power character is
\[
                   U^2=\left(\frac{A-1}{2A}\right)^N. \tag{9}
\]
In particular \(Y_iU=NU\). The factor \(2^N\), the power N,
and its marked root cannot be replaced by their value at one
point. Equation (9) is a SOURCE/frame character. It is not,
without the missing network map, the knot meridian's ADO
modified-dimension character.

## 5. The old cut-clock normal really detects this scale

The specified actual whole divided-source construction has a
concrete old-clock normal pairing, derived in
[the controlled Fourier/current dictionary](controlled_fourier_current_and_conormal_dictionary.md).
Let \(U_s(q;a,b)\) be its actual fixed-cut pairing and use the
root-one ratios \(U_0/U_s\) on the head strings. The resulting
UNNORMALIZED whole source satisfies
\[
 \Phi_Q(I)=U_0(q;a,b),\qquad
 \left[\frac{\Phi_Q(Q^SZ^R)}{1-Q^N}\right]_{Q_N}
       =\frac{((a+b)/2)^N}{N(1-Q_N)},\quad Z=Q^N.     \tag{10}
\]
With a=b=alpha its numerator is exactly U of (7).
The scalar multiplier is nonzero, has modulus between
\(1/(2\pi)\) and \(1/4\), and tends to \(-1/(2\pi i)\).

For completeness, put \(\delta=1-Q^N\). The per-string ratio
\(U_s(q;a,bZ)/U_s(q;a,b)\) has first coefficient
\(-N b/(a+b)\), independent of s at the root.
The sums \(\sum_sQ_N^s=0\) kill that contribution and all
overall source-unit derivatives. The remaining exact identity
\(\sum_s sQ_N^s=-N/(1-Q_N)\) proves (10).
The reduced head clock gives the same SELECTED scalar after
these cancellations, although its operator Ward commutators
differ. Thus (10) detects the scale line; it is not by itself
a new independent Fr scalar-current theorem.

Dividing the whole functional by U_0 returns the normalized
original same-high-color scalar. Retaining U_0 separately
keeps the actual source line and all its derivatives.
This compares the high color with itself; its off-root jets
are not equated with the low N-color jets.

## 6. The Kummer marking and remaining global comparison

The ACTUAL pure-power source is unchanged under
\((a,b)\mapsto(\zeta a,\zeta b)\), \(\zeta^N=1\).
Likewise the paired Sym^N data (3) know alpha^N, not alpha.
To use the standard Borel torsor and (5), retain the marked
Kummer cover \(\alpha^N=U\), anchored by alpha=1.
The unmarked actual Sym^N orbit is a homogeneous quotient
by this finite isotropy, which need not be normal in the Borel.
For N>2 it inherits neither a Borel quotient group nor a free
SL2 Borel torsor action; the central-sign N=2 exception is below.
The common marked SL2-Borel cover, rather than that quotient,
carries the free source action and the frame sign-cover map.

One cannot silently descend (5) to the unmarked Sym^N cone:
alpha^2 generally changes under a mu_N root when N>2.
Its frame sign cover only removes mu_2. At N=2 this subgroup
is central: the quotient does inherit the PGL2 Borel group and
its free torsor action, although the SL2 Borel action has kernel
mu_2. For N>2 the finite isotropy is not normal in the Borel,
so no quotient group structure is silently imposed. The unframed geometric
character is gauge-invariant, but the relative endpoints, log
sheets and period characters still require their own descent.
This is precisely why the root mark belongs to the source torsor.

At \(U=0\), or at the missing dual flag \(u=-1\), source vectors
and inverse duals cannot be specialized separately. The actual
paired fractional lattice or normal source complex must remain.
On a physical cut loop the scale may approach this boundary,
so no growing-neighborhood norm or cycle comparison follows
from the regular local torsor.

Equations (4), (6), (8), and (10) are concrete actual
source/framing data. The remaining theorem is specific: map
the whole network's ordinary/divided Ward currents and their
charged normal neighbors to these source forms, preserving
the final co-source and relative endpoints. The geometric
Gaussian coefficients and global selected contribution have
not been identified by an abstract Borel isomorphism.

[The exact audit](../experiments/audit_actual_frobenius_borel_torsor.py)
and [results](../experiments/actual_frobenius_borel_torsor_results.json)
check the ACTUAL divided-source and dual matrix fields,
scale/descendant pairings, frame pushforward, area form, and
co-source covariance in 63 symbolic checks at N=2 through 9.

